class ConversationState:

    def __init__(self):
        self.profile = {}
        self.current_intent = None
        self.pending_questions = []