from scheme_knowledge_base import SCHEMES

def evaluate_scheme(profile, scheme):

    score = 0
    uncertainty = 0

    rules = scheme["eligibility"]

    # AGE
    if "age_min" in rules:
        if "age" in profile:
            if profile["age"] >= rules["age_min"]:
                score += 40
            else:
                return -100, 0   # hard reject
        else:
            uncertainty += 1

    # RELIGION ONLY
    if "religion_only" in rules:
        if "religion" in profile:
            if profile["religion"] in rules["religion_only"]:
                score += 40
            else:
                return -100, 0
        else:
            uncertainty += 1

    # RELIGION EXCLUDE
    if "religion_exclude" in rules:
        if "religion" in profile:
            if profile["religion"] in rules["religion_exclude"]:
                return -100, 0
            else:
                score += 20
        else:
            uncertainty += 1

    # PREGNANT
    if rules.get("pregnant") == True:
        if "pregnant" in profile:
            if profile["pregnant"]:
                score += 40
            else:
                return -100, 0
        else:
            uncertainty += 1

    # LOW INCOME
    if "income_max" in rules:
        if profile.get("income_level") == "low":
            score += 25
        else:
            uncertainty += 1

    return score, uncertainty


def get_top_schemes(profile, intent):

    ranked = []

    for scheme in SCHEMES:

        if scheme["category"] != intent:
            continue

        score, uncertainty = evaluate_scheme(profile, scheme)

        # Reject only if strong conflict
        if score == -100:
            continue

        # Prefer schemes with higher certainty
        final_score = score - (uncertainty * 5)

        ranked.append((scheme, final_score, uncertainty))

    ranked.sort(key=lambda x: x[1], reverse=True)

    return ranked[:3]