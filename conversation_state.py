class ConversationState:

    def __init__(self, language="telugu"):
        self.profile = {}
        self.current_intent = None
        self.pending_questions = []
        self.intent = None
        self.language = language  # "telugu" or "english"