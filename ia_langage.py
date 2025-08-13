from gpt4all import GPT4All

class IALanguage:
    def __init__(self, model_name="gpt4all-lora"):
        self.model = GPT4All(model_name)

    def ask(self, prompt):
        return self.model.generate(prompt)
