from rapidfuzz import fuzz
import re

# ---------------- FUZZY MATCH ----------------
def similar(keyword, text, threshold=80):
    words = text.lower().split()
    for w in words:
        if fuzz.ratio(keyword, w) >= threshold:
            return True
    return False


# ---------------- YES / NO ----------------
YES_WORDS = ["yes", "avunu", "haa", "ha", "undi"]
NO_WORDS = ["no", "kaadu", "ledu"]

def interpret_binary_answer(text, expected_field):
    t = text.strip().lower()

    if t in YES_WORDS:
        if expected_field == "income_level":
            return {"income_level": "low"}
        return {expected_field: True}

    if t in NO_WORDS:
        return {expected_field: False}

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


# ---------------- MAIN EXTRACTION ----------------
def extract_attributes(text):

    text = text.lower()
    profile = {}

    # standalone number
    if text.strip().isdigit():
        profile["age"] = int(text.strip())

    # age with words
    age_match = re.search(r'(\d+)', text)
    if age_match:
        profile["age"] = int(age_match.group(1))

    telugu_age = telugu_text_to_number(text)
    if telugu_age:
        profile["age"] = telugu_age

    # Religion
    if similar("muslim", text):
        profile["religion"] = "muslim"

    if similar("hindu", text):
        profile["religion"] = "hindu"

    # Income
    if (similar("poor", text) or
        "dabbulu levu" in text or
        "income ledu" in text or
        "money problem" in text or
        similar("coolie", text)):
        profile["income_level"] = "low"

    # Widow
    if ("husband chachipoyaru" in text or
        similar("widow", text)):
        profile["widow"] = True

    # Divorce / Single
    if (similar("divorce", text) or
        similar("divorced", text) or
        "divorce ayyanu" in text or
        "vadilesadu" in text):
        profile["single_woman"] = True

    # Pregnancy
    if (similar("pregnant", text) or
        similar("delivery", text) or
        similar("baby", text)):
        profile["pregnant"] = True

    # Govt hospital
    if (similar("government", text) or similar("govt", text)):
        profile["delivery_in_govt_hospital"] = True

    # Serious illness
    if (similar("operation", text) or
        similar("cancer", text) or
        similar("kidney", text) or
        similar("heart", text)):
        profile["serious_illness"] = True
        profile["income_level"] = "low"

    # Skill
    if (similar("stitching", text) or
        similar("tailoring", text) or
        similar("machine", text)):
        profile["skill_in_tailoring"] = True

    # Domestic Violence
    if (similar("kottutadu", text) or
        similar("violence", text) or
        similar("torture", text) or
        similar("abuse", text)):
        profile["violence"] = True

    return profile