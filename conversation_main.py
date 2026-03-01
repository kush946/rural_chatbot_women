from transcribe import transcribe
from attribute_extractor import extract_attributes, interpret_binary_answer
from intent_classifier import detect_intent
from conversation_state import ConversationState
from scheme_matcher import get_top_schemes
from scheme_presenter import show_scheme
from question_engine import ask_question
from question_selector import next_best_question


# ---------------- INPUT MODE ----------------
def get_user_text():

    mode = input("\n1: Voice  2: Type\nChoose input mode: ")

    if mode == "1":
        print("Speak now (record audio into input_audio.wav)...")
        text = transcribe("input_audio.wav")
        return text

    return input("మీ సమాధానం: ")


# ---------------- MAIN FUNCTION ----------------
def run():

    state = ConversationState()

    # -------- FIRST QUERY --------
    text = get_user_text()
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

        question = ask_question(field)
        print("\nSystem:", question)

        reply = get_user_text()
        print("User:", reply)

        new_data = extract_attributes(reply)

        if not new_data:
            new_data = interpret_binary_answer(reply, field)

        state.profile.update(new_data)

        print("DEBUG PROFILE:", state.profile)

    # -------- SHOW TOP SCHEMES --------
    top = get_top_schemes(state.profile, state.intent)

    if not top:
        print("\nమీకు సరిపడే పథకం కనబడలేదు")
        return

    print("\n==============================")
    print("మీకు సరిపడే ముఖ్యమైన పథకాలు")
    print("==============================")

    for scheme, score, reasons in top:
        print("\n⭐ Relevance Score:", score)
        show_scheme(scheme)


# ---------------- START ----------------
if __name__ == "__main__":
    run()