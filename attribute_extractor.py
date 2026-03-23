from rapidfuzz import fuzz
import re

# ---------------- FUZZY MATCH ----------------
def similar(keyword, text, threshold=85):
    words = text.lower().split()
    for w in words:
        if fuzz.ratio(keyword, w) >= threshold:
            return True
    return False


# ---------------- YES / NO ----------------
YES_WORDS = ["yes", "avunu", "haa", "ha", "undi", "yep", "yeah", "sure", "okay", "ok", "true", "yup"]
NO_WORDS = ["no", "kaadu", "ledu", "nope", "nah", "false", "not"]

def interpret_binary_answer(text, expected_field):
    t = text.strip().lower()

    if t in YES_WORDS:
        if expected_field == "income_level":
            return {"income_level": "low"}
        return {expected_field: True}

    if t in NO_WORDS:
        return {expected_field: False}

    # If it's a number field (like num_children)
    if expected_field == "num_children":
        if t.isdigit():
            num = int(t)
            if 0 <= num <= 20:
                return {"num_children": num}

    # If it's community field
    if expected_field == "community":
        if "sc" in t:
            return {"community": "sc"}
        elif "st" in t:
            return {"community": "st"}
        elif "bc" in t:
            return {"community": "bc"}
        elif "ebc" in t:
            return {"community": "ebc"}

    return {}


# ---------------- TELUGU NUMBER PARSER ----------------
TELUGU_UNITS = {
    "సున్నా":0,"ఒకటి":1,"రెండు":2,"మూడు":3,"నాలుగు":4,"ఐదు":5,
    "ఆరు":6,"ఏడు":7,"ఎనిమిది":8,"తొమ్మిది":9
}

TELUGU_TEENS = {
    "పది":10,"పదకొండు":11,"పన్నెండు":12,"పదమూడు":13,"పద్నాలుగు":14,
    "పదిహేను":15,"పదహారు":16,"పదిహేడు":17,"పద్దెనిమిది":18,"పంతొమ్మిది":19
}

TELUGU_TENS = {
    "ఇరవై":20,"ముప్పై":30,"నలభై":40,"యాభై":50,
    "అరవై":60,"డెబ్బై":70,"ఎనభై":80,"తొంభై":90
}

TELUGU_HUNDRED = {
    "వంద":100,"నూరు":100
}

def telugu_text_to_number(text):
    words = text.split()
    total = 0
    current = 0

    for w in words:
        if w in TELUGU_UNITS:
            current += TELUGU_UNITS[w]
        elif w in TELUGU_TEENS:
            current += TELUGU_TEENS[w]
        elif w in TELUGU_TENS:
            current += TELUGU_TENS[w]
        elif w in TELUGU_HUNDRED:
            if current == 0:
                current = 1
            current *= 100

    total += current
    return total if total != 0 else None


# ---------------- AGE VALIDATION ----------------
def is_valid_age(age):
    """Validate age is within reasonable range (1-120)"""
    return isinstance(age, int) and 1 <= age <= 120


# -------- INCOME PARSING --------
def parse_income_amount(text):
    """Extract and parse income amounts from text (handles Indian format)"""
    import re
    
    # Common income thresholds for low income (in Rs)
    LOW_INCOME_THRESHOLD = 300000  # 3 lakhs - generous threshold for rural schemes
    
    # Pattern: Rs. followed by numbers in Indian format (1,00,000)
    # This matches: Rs. 1,00,000 or Rs 100000 or Rs 1 lakh, etc.
    patterns = [
        # Indian format: Rs. X,XX,XXX
        (r'rs\.?\s*([\d,]+)', 1),
        # Lakh format: 1 lakh, 2 lakhs
        (r'(\d+)\s*(?:lakhs?|lacs?)', 100000),
    ]
    
    for pattern, multiplier in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            amount_str = match.group(1)
            # Remove commas for conversion
            amount_str = amount_str.replace(',', '')
            try:
                amount = float(amount_str) * multiplier
                if amount > 0:
                    return amount
            except ValueError:
                continue
    
    return None


# -------- MAIN EXTRACTION ----------------
def extract_attributes(text):

    text_lower = text.lower()
    profile = {}

    # standalone number
    if text_lower.strip().isdigit():
        age = int(text_lower.strip())
        if is_valid_age(age):
            profile["age"] = age

    # age with words (only if not already set)
    if "age" not in profile:
        # Use lookahead/lookbehind to avoid matching after minus sign
        age_match = re.search(r'(?<![0-9\-])(\d+)(?![0-9])', text_lower)
        if age_match:
            age = int(age_match.group(1))
            # Avoid matching gestational weeks/months
            if not any(word in text_lower for word in ["week", "month", "trimester"]):
                if is_valid_age(age):
                    profile["age"] = age

    # telugu number parsing (only if not already set)
    if "age" not in profile:
        telugu_age = telugu_text_to_number(text_lower)
        if telugu_age and is_valid_age(telugu_age):
            profile["age"] = telugu_age

    # Religion
    if similar("muslim", text_lower):
        profile["religion"] = "muslim"

    if similar("hindu", text_lower):
        profile["religion"] = "hindu"

    # Income - check for income amount first
    income_amount = parse_income_amount(text_lower)
    if income_amount and income_amount < 300000:  # Low income threshold
        profile["income_level"] = "low"
    
    # Income - check for keywords
    if (similar("poor", text_lower) or
        similar("low", text_lower) and "income" in text_lower or
        "low income" in text_lower or
        "dabbulu levu" in text_lower or
        "income ledu" in text_lower or
        "money problem" in text_lower or
        similar("coolie", text_lower) or
        similar("needy", text_lower) or
        similar("poverty", text_lower) or
        "low earnings" in text_lower or
        "no money" in text_lower):
        profile["income_level"] = "low"

    # Widow
    if ("husband chachipoyaru" in text_lower or
        similar("widow", text_lower) or
        "husband dead" in text_lower or
        "husband passed" in text_lower or
        "husband died" in text_lower):
        profile["widow"] = True

    # Divorce / Single
    if (similar("divorce", text_lower) or
        similar("divorced", text_lower) or
        similar("single", text_lower) or
        "divorce ayyanu" in text_lower or
        "vadilesadu" in text_lower or
        "unmarried" in text_lower or
        "separated" in text_lower):
        profile["single_woman"] = True

    # Pregnancy
    if (similar("pregnant", text_lower) or
        similar("pregnancy", text_lower) or
        similar("delivery", text_lower) or
        similar("baby", text_lower) or
        similar("expecting", text_lower) or
        similar("maternity", text_lower) or
        "in pregnancy" in text_lower or
        similar("lactating", text_lower) or
        similar("breastfeeding", text_lower)):
        profile["pregnant"] = True

    # Govt hospital
    if (similar("government", text_lower) or 
        similar("govt", text_lower) or
        similar("public hospital", text_lower) or
        "government hospital" in text_lower):
        profile["delivery_in_govt_hospital"] = True

    # Serious illness
    if (similar("operation", text_lower) or
        similar("cancer", text_lower) or
        similar("kidney", text_lower) or
        similar("heart", text_lower) or
        similar("surgery", text_lower) or
        similar("disease", text_lower) or
        similar("illness", text_lower) or
        "health problem" in text_lower):
        profile["serious_illness"] = True
        profile["income_level"] = "low"

    # Skill
    if (similar("stitching", text_lower) or
        similar("tailoring", text_lower) or
        similar("machine", text_lower) or
        similar("sewing", text_lower) or
        similar("tailor", text_lower)):
        profile["skill_in_tailoring"] = True

    # Domestic Violence
    if (similar("kottutadu", text_lower) or
        similar("violence", text_lower) or
        similar("torture", text_lower) or
        similar("abuse", text_lower) or
        similar("beating", text_lower) or
        similar("beaten", text_lower) or
        "hit by" in text_lower or
        "beaten by" in text_lower):
        profile["violence"] = True

    # Gender
    if similar("man", text_lower) or similar("male", text_lower) or similar("boy", text_lower):
        profile["gender"] = "male"
    elif similar("woman", text_lower) or similar("female", text_lower) or similar("girl", text_lower) or similar("lady", text_lower):
        profile["gender"] = "female"

    # Community (Caste)
    if similar("scheduled caste", text_lower) or similar("sc", text_lower):
        profile["community"] = "sc"
    elif similar("scheduled tribe", text_lower) or similar("st", text_lower):
        profile["community"] = "st"
    elif similar("backward", text_lower) or similar("bc", text_lower):
        profile["community"] = "bc"
    elif similar("extremely backward", text_lower) or similar("ebc", text_lower):
        profile["community"] = "ebc"

    # Number of children (extract digit if present)
    if "children" in text_lower or "pillalu" in text_lower or "kids" in text_lower:
        num_match = re.search(r'(\d+)', text_lower)
        if num_match:
            num = int(num_match.group(1))
            if 0 <= num <= 20:  # reasonable range
                profile["num_children"] = num

    return profile