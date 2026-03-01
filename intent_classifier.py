from rapidfuzz import fuzz

def similar(word, text, threshold=80):
    for w in text.split():
        if fuzz.ratio(word, w) >= threshold:
            return True
    return False


def detect_intent(text):

    text = text.lower()

    # -------- VIOLENCE --------
    if any([
        similar("kottutadu", text),
        similar("violence", text),
        similar("torture", text),
        similar("abuse", text)
    ]):
        return "violence_support", 1.0


    # -------- PENSION --------
    if any([
        similar("widow", text),
        similar("vidow", text),
        similar("pension", text),
        similar("penshan", text),
        similar("penshon", text),
        similar("old", text)
    ]):
        return "pension_support", 1.0


    # -------- MARRIAGE --------
    if any([
        similar("pelli", text),
        similar("marriage", text),
        similar("shaadi", text)
    ]):
        return "marriage_support", 1.0


    # -------- PREGNANCY --------
    if any([
        similar("pregnant", text),
        similar("delivery", text),
        similar("baby", text),
        similar("garbham", text)
    ]):
        return "pregnancy_support", 1.0


    # -------- HEALTH --------
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


    return "unknown", 0.0