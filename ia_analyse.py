class IAAnalyse:
    def __init__(self, language_module):
        self.lang = language_module

    def learn_from_text(self, text):
        # ici tu utiliseras GPT local ou autre module IA
        # exemple simplifié
        return f"# Nouveau code basé sur : {text[:30]}..."
