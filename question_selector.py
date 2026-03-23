from scheme_knowledge_base import SCHEMES

# order matters → most important first
PRIORITY_ORDER = [
    "age",
    "income_level",
    "religion",
    "pregnant",
    "widow",
    "single_woman",
    "delivery_in_govt_hospital",
    "serious_illness",
    "skill_in_tailoring",
    "minority_woman",
    "num_children",
    "community"
]


def required_fields_from_scheme(scheme):

    rules = scheme["eligibility"]
    needed = set()

    for key in rules.keys():

        if key == "age_min":
            needed.add("age")

        elif key == "income_max":
            needed.add("income_level")

        elif key in ["religion_only", "religion_exclude"]:
            needed.add("religion")

        else:
            needed.add(key)

    return needed


def next_best_question(profile, intent):

    required = set()

    for scheme in SCHEMES:
        if scheme["category"] != intent:
            continue

        required |= required_fields_from_scheme(scheme)

    # Filter out gender-specific questions if gender is known
    gender = profile.get("gender")
    if gender == "male":
        required.discard("widow")
        required.discard("single_woman")
        required.discard("minority_woman")
        required.discard("woman")
    # If female or unknown, keep them (assume female if unknown for safety)

    # ask highest priority missing field
    for field in PRIORITY_ORDER:
        if field in required and field not in profile:
            return field

    return None