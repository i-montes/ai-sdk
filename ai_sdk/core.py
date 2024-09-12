class AIModel:
    def __init__(self, provider):
        self.provider = provider
    
    def generate_text(self, prompt, **kwargs):
        return self.provider.generate_text(prompt, **kwargs)

    def stream_response(self, prompt, **kwargs):
        return self.provider.stream_response(prompt, **kwargs)
