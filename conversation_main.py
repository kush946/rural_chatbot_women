from transcribe import transcribe
from attribute_extractor import extract_attributes, interpret_binary_answer
from intent_classifier import detect_intent
from conversation_state import ConversationState
from scheme_matcher import get_top_schemes
from scheme_presenter import show_scheme
from question_engine import ask_question
from question_selector import next_best_question


# ---------------- LANGUAGE SELECTION ----------------
def select_language():
    """Ask user to select preferred language"""
    print("\n" + "=" * 50)
    print("Welcome to Rural Voice App")
    print("=" * 50)
    print("\nSelect language / భాష ఎంచుకోండి:")
    print("1: English")
    print("2: తెలుగు (Telugu)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "2":
        return "telugu"
    return "english"


# ---------------- INPUT MODE ----------------
def get_user_text(language="telugu"):
    """Get text input from user, supporting voice or typing"""
    
    if language == "english":
        mode = input("\n1: Voice  2: Type\nChoose input mode: ").strip()
        if mode == "1":
            print("Speak now (record audio into input_audio.wav)...")
            text = transcribe("input_audio.wav", language="english")
            return text
        return input("Your answer: ")
    else:
        mode = input("\n1: వాయిస్  2: టైప్\nఇన్‌పుట్ మోడ్ ఎంచుకోండి: ").strip()
        if mode == "1":
            print("ఇప్పుడు మాట్లాడండి (input_audio.wav లోకి ఆడియో రికార్డ్ చేయండి)...")
            text = transcribe("input_audio.wav", language="telugu")
            return text
        return input("మీ సమాధానం: ")


# ------------ SHOW RESULTS MESSAGE -----------
def show_no_schemes_message(language="telugu"):
    """Show message when no schemes found"""
    if language == "english":
        print("\nNo suitable schemes found for you.")
    else:
        print("\nమీకు సరిపడే పథకం కనబడలేదు")


def show_schemes_header(language="telugu"):
    """Show header for scheme results"""
    if language == "english":
        print("\n==============================")
        print("Top Schemes For You")
        print("==============================")
    else:
        print("\n==============================")
        print("మీకు సరిపడే ముఖ్యమైన పథకాలు")
        print("==============================")


# ---------------- MAIN FUNCTION ----------------
def run():
    # Select language first
    language = select_language()
    
    state = ConversationState(language=language)

    # -------- FIRST QUERY --------
    text = get_user_text(language=language)
    print("User:", text)

    intent, _ = detect_intent(text)
    print("DEBUG INTENT:", intent)
    state.intent = intent

    profile_data = extract_attributes(text)

    # -------- EMERGENCY CHECK --------
    if profile_data.get("violence"):
        from emergency_support import show_emergency_help
        show_emergency_help()
        return

    state.profile.update(profile_data)

    # -------- SMART QUESTION LOOP --------
    while True:

        field = next_best_question(state.profile, state.intent)

        # No more useful questions → show results
        if not field:
            break

        question = ask_question(field, language=language)
        print("\nSystem:", question)

        reply = get_user_text(language=language)
        print("User:", reply)

        new_data = extract_attributes(reply)

        if not new_data:
            new_data = interpret_binary_answer(reply, field)

        state.profile.update(new_data)

        print("DEBUG PROFILE:", state.profile)

    # -------- SHOW TOP SCHEMES --------
    top = get_top_schemes(state.profile, state.intent)

    if not top:
        show_no_schemes_message(language)
        return

    show_schemes_header(language)

    for scheme, score, reasons in top:
        if language == "english":
            print(f"\n⭐ Relevance Score: {score}")
        else:
            print(f"\n⭐ సంబంధితత్వ స్కోర్: {score}")
        show_scheme(scheme, language=language)


# ---------------- START ----------------
if __name__ == "__main__":
    run()