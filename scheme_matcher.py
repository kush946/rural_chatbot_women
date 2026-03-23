from scheme_knowledge_base import SCHEMES

def evaluate_scheme(profile, scheme):

    score = 0
    uncertainty = 0

    rules = scheme["eligibility"]

    # AGE MINIMUM
    if "age_min" in rules:
        if "age" in profile:
            if profile["age"] >= rules["age_min"]:
                score += 40
            else:
                return -100, 0   # hard reject
        else:
            uncertainty += 1

    # AGE MAXIMUM
    if "age_max" in rules:
        if "age" in profile:
            if profile["age"] <= rules["age_max"]:
                score += 20
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
            uncertainty += 2

    # PREGNANT
    if rules.get("pregnant") == True:
        if "pregnant" in profile:
            if profile["pregnant"]:
                score += 40
            else:
                return -100, 0
        else:
            uncertainty += 1

    # PREGNANT OR LACTATING (alternate field)
    if rules.get("pregnant_or_lactating") == True:
        if profile.get("pregnant"):  # simplified - treating lactating same as pregnant
            score += 40
        else:
            uncertainty += 1

    # WIDOW
    if rules.get("widow") == True:
        if "widow" in profile:
            if profile["widow"]:
                score += 40
            else:
                return -100, 0
        else:
            uncertainty += 1

    # SINGLE WOMAN
    if rules.get("single_woman") == True:
        if "single_woman" in profile:
            if profile["single_woman"]:
                score += 40
            else:
                return -100, 0
        else:
            uncertainty += 1

    # DELIVERY IN GOVT HOSPITAL
    if rules.get("delivery_in_govt_hospital") == True:
        if "delivery_in_govt_hospital" in profile:
            if profile["delivery_in_govt_hospital"]:
                score += 30
            else:
                uncertainty += 1
        else:
            uncertainty += 1

    # SERIOUS ILLNESS
    if rules.get("serious_illness") == True:
        if "serious_illness" in profile:
            if profile["serious_illness"]:
                score += 30
            else:
                return -100, 0
        else:
            uncertainty += 1

    # SKILL IN TAILORING
    if rules.get("skill_in_tailoring") == True:
        if "skill_in_tailoring" in profile:
            if profile["skill_in_tailoring"]:
                score += 25
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

    # LOW INCOME FAMILY (alternate field name)
    if rules.get("low_income_family") == True:
        if profile.get("income_level") == "low":
            score += 25
        else:
            uncertainty += 1

    # MINORITY WOMAN
    if rules.get("minority_woman") == True:
        if "religion" in profile:
            # Muslim, Christian, Sikh, Buddhist, Jain are minorities
            if profile["religion"] in ["muslim", "christian", "sikh", "buddhist", "jain"]:
                score += 30
            else:
                return -100, 0
        else:
            uncertainty += 1

    # WOMAN (generic - any woman)
    if rules.get("woman") == True:
        # Assuming profile is for a woman (would need gender field for full accuracy)
        score += 15  # slight boost if scheme is woman-specific

    # CHILDREN LIMIT (only if user has provided this info)
    if "children_limit" in rules:
        if "num_children" in profile:
            if profile["num_children"] <= rules["children_limit"]:
                score += 20
            else:
                return -100, 0
        else:
            uncertainty += 1

    # COMMUNITY (SC/ST/BC/EBC)
    if "community" in rules:
        if "community" in profile:
            if profile["community"] in rules["community"]:
                score += 40
            else:
                return -100, 0
        else:
            uncertainty += 2

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