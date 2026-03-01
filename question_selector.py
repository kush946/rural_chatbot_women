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
    "skill_in_tailoring"
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

    # ask highest priority missing field
    for field in PRIORITY_ORDER:
        if field in required and field not in profile:
            return field

    return None