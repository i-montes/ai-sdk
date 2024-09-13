class AIModel:
    def __init__(self, provider):
        self.provider = provider
    
    def use_text(self, prompt, **kwargs):
        return True #self.provider.generate_text(prompt, **kwargs)
    
    # def use_object(self, prompt, **kwargs):
    #     return True #self.provider.generate_text(prompt, **kwargs)
    
    # def use_assistant(self, prompt, **kwargs):
    #     return True #self.provider.use-assistant(prompt, **kwargs)
    
    
    # def use_completion(self, prompt, **kwargs):
    #     return True #self.provider.use_completion(prompt, **kwargs)
    
    # def use_chat(self, prompt, **kwargs):
    #     return True #self.provider.use_chat(prompt, **kwargs)