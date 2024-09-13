from typing import Optional, Mapping, AnyStr
from .response import OllamaResponseProcessor
import ollama


class OllamaProvider:
    def __init__(self, model: str):
        """
        Inicializa la instancia de OllamaProvider con un modelo específico y parámetros del sistema.

        Args:
            model (str): El nombre del modelo AI a utilizar (por ejemplo, "llama", "gpt").
        """
        self.model = model
       
    def generate_text(self, 
            prompt: str, 
            system: Optional[str] = '', 
            max_retries: Optional[int] = 3
        ) -> OllamaResponseProcessor:
        """
        Genera texto utilizando el modelo AI especificado. Envía un prompt y mensajes previos al modelo y devuelve el resultado generado.

        Args:
            prompt (str): El texto inicial que se enviará al modelo como base para la generación.
            system (Optional[str]): Opcional. El sistema de generación de texto. Por defecto, es None.
            max_retries (Optional[int]): Opcional. El número máximo de intentos en caso de fallo de la solicitud. Por defecto, es 3.

        Returns:
            str: El texto generado por el modelo basado en el prompt y los mensajes proporcionados.

        Raises:
            ValueError: Si el prompt o los mensajes están vacíos.
            ConnectionError: Si se alcanza el número máximo de intentos sin éxito.
            Exception: Si ocurre un error no controlado.
        """
        if not prompt:
            raise ValueError("El argumento 'prompt' no puede estar vacío.")
       
        attempt = 0
        while attempt < (max_retries or 3):
            try:
                # Simulación de la llamada a un API para generar el texto
                response = self.__send_request(prompt=prompt, system=system)

                # Aquí se puede analizar y manejar la respuesta en caso de errores específicos
                # if "error" in response:
                #     raise ConnectionError("Error en la solicitud a la API: " + response["error"])

                return response
            
            except ConnectionError as e:
                attempt += 1
                if attempt >= (max_retries or 3):
                    raise ConnectionError(f"Error de conexión tras {max_retries} intentos: {e}")
            except Exception as e:
                raise Exception(f"Ocurrió un error inesperado: {e}")
        
    def __send_request(self, 
            prompt: str = '',
            system: str = '',
        ) -> OllamaResponseProcessor:
        """
        Args:
            system (str): El sistema que describe el contexto de la conversación.
            prompt (str): El texto inicial enviado al modelo.

        Returns:
            model (str): El nombre del modelo AI utilizado.
            response (str): El texto generado por el modelo basado en el prompt y los mensajes proporcionados.
            done (bool): True si el modelo ha finalizado la generación de texto, False en caso contrario.
            done_reason (str): La razón por la que el modelo ha finalizado la generación de texto.
            context (str): El contexto actual del modelo.
            total_duration (int): La duración total de la generación de texto.
            load_duration (int): La duración de la carga del modelo.
            prompt_eval_count (int): Número de tokens en el prompt.
            prompt_eval_duration (int): Tiempo dedicado en nanosegundos evaluando el mensaje.
            eval_count (int): Número de tokens generados por la generación de texto.
            tokens_per_second (int): Número de tokens por segundo generados por la generación de texto.
        """
        
        try:
            res = ollama.generate(model=self.model, system=system, prompt=prompt)
        

            return OllamaResponseProcessor(res)

        except Exception as e:
            raise e