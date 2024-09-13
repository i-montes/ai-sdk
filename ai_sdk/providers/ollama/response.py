from ._types import ResponseDataType

class OllamaResponseProcessor:
    def __init__(self, res: ResponseDataType):
        """
        Inicializa la clase con el resultado JSON devuelto por Ollama.

        Args:
            res (dict): El resultado JSON devuelto por Ollama.
        """
        self.model = res.get('model')
        self.response = res.get('response')
        self.done = res.get('done')
        self.done_reason = res.get('done_reason')
        self.context = res.get('context')
        self.total_duration = res.get('total_duration')
        self.load_duration = res.get('load_duration')
        self.prompt_eval_count = res.get('prompt_eval_count')
        self.prompt_eval_duration = res.get('prompt_eval_duration')
        self.eval_count = res.get('eval_count')
        self.eval_duration = res.get('eval_duration')
        self.tokens_per_second = (self.eval_count / self.eval_duration) * 10**9 if self.eval_duration else 0
        
    def __str__(self) -> str:
        return self.response

    def process_response(self) -> dict:
        """
        Procesa la respuesta para devolver el formato esperado.

        Returns:
            dict: Un diccionario con la respuesta procesada y metadatos.
        """

        return {
            "text": self.response,
            "meta": {
                "model": self.model,
                "done": self.done,
                "done_reason": self.done_reason,
                "context": self.context,
                "total_duration": self.total_duration,
                "load_duration": self.load_duration,
                "prompt_eval_count": self.prompt_eval_count,
                "prompt_eval_duration": self.prompt_eval_duration,
                "eval_count": self.eval_count,
                "tokens_per_second": self.tokens_per_second
            }
        }
