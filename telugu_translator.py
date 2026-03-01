FIELD_MAP = {
    "name": "పథకం పేరు",
    "benefits": "లాభాలు",
    "application": "దరఖాస్తు విధానం",
    "documents": "అవసరమైన పత్రాలు",
    "notes": "గమనికలు"
}


WORD_MAP = {
    "Monthly pension": "నెలసరి పెన్షన్",
    "financial assistance": "ఆర్థిక సహాయం",
    "Apply": "దరఖాస్తు చేయాలి",
    "through": "ద్వారా",
    "government hospital": "ప్రభుత్వ ఆసుపత్రి",
    "Free medical treatment": "ఉచిత వైద్య చికిత్స",
    "loan": "రుణం",
    "pregnancy": "గర్భధారణ",
    "marriage": "వివాహం"
}


def to_telugu(text):

    if not isinstance(text, str):
        return text

    output = text

    for eng, tel in WORD_MAP.items():
        output = output.replace(eng, tel)

    return output