def telugu_money_line(text):

    if "₹" in text:
        # extract amount
        return "ప్రభుత్వం నుండి ఆర్థిక సహాయం మరియు శిశు సంరక్షణ కిట్ అందుతుంది"

    return text


def telugu_documents(doc):
    MAP = {
        "Aadhaar": "ఆధార్ కార్డ్",
        "Aadhaar Card": "ఆధార్ కార్డ్",
        "Bank Passbook": "బ్యాంక్ పాస్‌బుక్",
        "Bank Details": "బ్యాంక్ ఖాతా వివరాలు",
        "Income Certificate": "ఆదాయ ధృవీకరణ పత్రం",
        "Caste Certificate": "జాతి ధృవీకరణ పత్రం",
        "Age Proof": "వయస్సు ధృవీకరణ పత్రం",
        "Mobile Number": "మొబైల్ నంబర్",
        "Death Certificate": "మరణ ధృవీకరణ పత్రం",
        "Pregnancy Checkup Proof": "గర్భ పరీక్ష పత్రం",
        "Ration Card": "రేషన్ కార్డు"
    }
    return MAP.get(doc, doc)


def telugu_benefits(text):

    text = text.lower()

    if "pension" in text:
        return "ప్రతి నెల ప్రభుత్వం నుండి పెన్షన్ అందుతుంది"

    if "marriage" in text:
        return "వివాహానికి ప్రభుత్వం ఆర్థిక సహాయం అందిస్తుంది"

    if "nutrition" in text:
        return "పోషకాహార కిట్ మరియు ఆరోగ్య ఆహారం అందుతుంది"

    if "treatment" in text:
        return "ఉచిత వైద్య చికిత్స ప్రభుత్వం ద్వారా అందుతుంది"

    if "machine" in text:
        return "ఉచిత కుట్టు యంత్రం అందించబడుతుంది"

    if "kit" in text:
        return "తల్లి మరియు శిశువు కోసం కిట్ మరియు ఆర్థిక సహాయం అందుతుంది"

    return telugu_money_line(text)


def telugu_application(text):

    text = text.lower()

    if "hospital" in text:
        return "సమీప ప్రభుత్వ ఆసుపత్రిలో నమోదు చేసుకోవాలి"

    if "meeseva" in text:
        return "మీసేవా కేంద్రంలో దరఖాస్తు చేయాలి"

    if "anganwadi" in text:
        return "అంగన్వాడి కేంద్రంలో నమోదు చేసుకోవాలి"

    if "portal" in text or "online" in text:
        return "ఆన్‌లైన్ ద్వారా దరఖాస్తు చేయాలి"

    return text


def telugu_notes(text):

    text = text.lower()

    if "government hospital" in text:
        return "ప్రభుత్వ ఆసుపత్రిలో ప్రసవం చేసిన వారికి మాత్రమే వర్తిస్తుంది"

    if "minority" in text:
        return "మైనారిటీ మహిళలకు మాత్రమే వర్తిస్తుంది"

    return text


def show_scheme(scheme):

    print("\n==============================")
    print("📌 పథకం పేరు:", scheme["name"])
    print("==============================")

    print("\n🟢 లాభాలు:")
    print(telugu_benefits(scheme["benefits"]))

    print("\n📝 దరఖాస్తు విధానం:")
    print(telugu_application(scheme["application"]))

    print("\n📄 అవసరమైన పత్రాలు:")
    for doc in scheme["documents"]:
        print("-", telugu_documents(doc))

    print("\n⚠️ గమనిక:")
    print(telugu_notes(scheme["notes"]))