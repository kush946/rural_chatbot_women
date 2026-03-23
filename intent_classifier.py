from rapidfuzz import fuzz

def similar(word, text, threshold=85):
    for w in text.split():
        if fuzz.ratio(word, w) >= threshold:
            return True
    return False


def detect_intent(text):

    text = text.lower()

    # -------- VIOLENCE --------
    # include English and Telugu verbs for beating/abuse
    if any([
        similar("kottutadu", text),
        similar("violence", text),
        similar("torture", text),
        similar("abuse", text),
        similar("beat", text),             # catches beat/beats/beating
        similar("beating", text),
        similar("beats", text),
        similar("spouse", text)
    ]):
        return "violence_support", 1.0

    # -------- MARRIAGE (check before pension to avoid "old" false positives) --------
    if any([
        similar("pelli", text),
        similar("marriage", text),
        similar("married", text),
        similar("marry", text),
        similar("wedding", text),
        similar("bride", text),
        similar("groom", text),
        similar("shaadi", text)
    ]):
        return "marriage_support", 1.0

    # -------- PREGNANCY --------
    if any([
        similar("pregnant", text),
        similar("pregnancy", text),
        similar("delivery", text),
        similar("baby", text),
        similar("garbham", text)
    ]):
        return "pregnancy_support", 1.0

    # -------- NUTRITION --------
    if any([
        similar("lactating", text),
        similar("breastfeeding", text),
        similar("nutrition", text),
        similar("anganwadi", text),
        similar("milk", text)
    ]):
        return "nutrition_support", 1.0
    if any([
        similar("operation", text),
        similar("cancer", text),
        similar("kidney", text),
        similar("heart", text),
        similar("treatment", text)
    ]):
        return "health_support", 1.0

    # -------- JOB --------
    if any([
        similar("job", text),
        similar("business", text),
        similar("loan", text),
        similar("machine", text),
        similar("stitching", text)
    ]):
        return "employment_support", 1.0

    # -------- PENSION (checked after more specific intents) --------
    if any([
        similar("widow", text),
        similar("vidow", text),
        similar("pension", text),
        similar("penshan", text),
        similar("penshon", text),
        # "old" is checked more carefully - need it in pension context
        ("old age" in text or "i am old" in text or "senior citizen" in text or "old" in text)
    ]):
        return "pension_support", 1.0

    return "unknown", 0.0