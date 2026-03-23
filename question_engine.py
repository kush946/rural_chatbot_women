def ask_question(field, language="telugu"):
    """Get question in requested language"""
    
    QUESTIONS = {
        "age": {
            "telugu": "మీ వయస్సు ఎంత?",
            "english": "What is your age?"
        },
        "income_level": {
            "telugu": "మీ కుటుంబ ఆదాయం తక్కువ వర్గంలోకి వస్తుందా? (అవును / కాదు)",
            "english": "Is your family income low? (Yes / No)"
        },
        "religion": {
            "telugu": "మీ మతం ఏమిటి? (హిందూ / ముస్లిం / క్రైస్తవ)",
            "english": "What is your religion? (Hindu / Muslim / Christian)"
        },
        "widow": {
            "telugu": "మీ భర్త మరణించారా? (అవును / కాదు)",
            "english": "Is your husband deceased? (Yes / No)"
        },
        "single_woman": {
            "telugu": "మీరు విడాకులు పొందారా లేదా ఒంటరిగా ఉంటున్నారా? (అవును / కాదు)",
            "english": "Are you divorced or single? (Yes / No)"
        },
        "pregnant": {
            "telugu": "మీరు గర్భవతిగా ఉన్నారా? (అవును / కాదు)",
            "english": "Are you pregnant? (Yes / No)"
        },
        "delivery_in_govt_hospital": {
            "telugu": "ప్రభుత్వ ఆసుపత్రిలో డెలివరీ చేయాలనుకుంటున్నారా? (అవును / కాదు)",
            "english": "Do you want delivery at a government hospital? (Yes / No)"
        },
        "serious_illness": {
            "telugu": "మీకు పెద్ద ఆపరేషన్ లేదా తీవ్రమైన వ్యాధి ఉందా? (అవును / కాదు)",
            "english": "Do you have a serious illness or need surgery? (Yes / No)"
        },
        "skill_in_tailoring": {
            "telugu": "మీకు కుట్టు పని (టైలరింగ్) వచ్చా? (అవును / కాదు)",
            "english": "Do you have tailoring skills? (Yes / No)"
        },
        "minority_woman": {
            "telugu": "మీరు మైనారిటీ వర్గానికి చెందారా? (అవును / కాదు)",
            "english": "Are you from a minority community? (Yes / No)"
        },
        "woman": {
            "telugu": "మీరు మహిళా కుటుంబ ప్రధానులా? (అవును / కాదు)",
            "english": "Are you the head of a woman-headed family? (Yes / No)"
        },
        "pregnant_or_lactating": {
            "telugu": "మీరు గర్భిణి లేదా బాలింతలా ఉన్నారా? (అవును / కాదు)",
            "english": "Are you pregnant or lactating? (Yes / No)"
        },
        "num_children": {
            "telugu": "మీకు ఎన్ని పిల్లలు ఉన్నారు?",
            "english": "How many children do you have?"
        },
        "community": {
            "telugu": "మీరు ఏ సమాజానికి చెందారు? (SC / ST / BC / EBC)",
            "english": "What is your community? (SC / ST / BC / EBC)"
        }
    }

    lang = language if language in ["telugu", "english"] else "telugu"
    if field in QUESTIONS:
        return QUESTIONS[field].get(lang, QUESTIONS[field]["telugu"])
    
    if lang == "english":
        return "Please provide more information"
    else:
        return "కొంచెం మరింత సమాచారం ఇవ్వండి"