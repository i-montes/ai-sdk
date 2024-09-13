from typing import List, Union, Optional, Dict, Sequence, Literal, Mapping, AnyStr
from ._types import OptionsOllama
import ollama
class OllamaProvider:
    def __init__(self, model: str, system: str, headers: Optional[Dict[str, str]] = None):
        """
        Inicializa la instancia de OllamaProvider con un modelo específico y parámetros del sistema.

        Args:
            model (str): El nombre del modelo AI a utilizar (por ejemplo, "llama", "gpt").
            system (str): El mensaje del sistema que describe el contexto de la conversación.
            headers (Optional[Dict[str, str]]): Opcional. Encabezados HTTP adicionales para las solicitudes API.
        """
        self.model = model
       
    def generate_text(self, system: Optional[str], prompt: str, headers: Optional[Dict[str, str]],  max_tokens: Optional[int] = 100, temperature: Optional[float] = 0.7, top_p: Optional[float] = 1.0, top_k: Optional[int] = None, max_retries: Optional[int] = 3) -> str:
        """
        Genera texto utilizando el modelo AI especificado. Envía un prompt y mensajes previos al modelo y devuelve el resultado generado.

        Args:
            prompt (str): El texto inicial que se enviará al modelo como base para la generación.
            messages (List[Dict[str, Union[str, List[Dict[str, Union[str, bytes]]]]]]): Una lista de mensajes que contiene el historial de la conversación. Cada mensaje debe tener el rol ("system", "user", "assistant") y el contenido correspondiente.
            max_tokens (Optional[int]): Opcional. El número máximo de tokens que se pueden generar. Por defecto, es 100.
            temperature (Optional[float]): Opcional. Controla la aleatoriedad de las respuestas. Un valor más alto (por ejemplo, 1.0) hace que las respuestas sean más creativas, mientras que un valor más bajo (por ejemplo, 0.2) las hace más deterministas. Por defecto, es 0.7.
            top_p (Optional[float]): Opcional. Controla la selección de tokens usando el muestreo de "nucleus". Un valor de 1.0 significa no limitar el muestreo. Por defecto, es 1.0.
            top_k (Optional[int]): Opcional. Limita el número de tokens de mayor probabilidad a considerar durante la generación. Si es `None`, no se aplica esta limitación.
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
                response = self._send_request(system=system, prompt=prompt, headers=headers)

                # Aquí se puede analizar y manejar la respuesta en caso de errores específicos
                if "error" in response:
                    raise ConnectionError("Error en la solicitud a la API: " + response["error"])

                return response["generated_text"]
            
            except ConnectionError as e:
                attempt += 1
                if attempt >= (max_retries or 3):
                    raise ConnectionError(f"Error de conexión tras {max_retries} intentos: {e}")
            except Exception as e:
                raise Exception(f"Ocurrió un error inesperado: {e}")
        
    def _send_request(self, 
            system: str = '',
            prompt: str = '',
            suffix: str = '',
            template: str = '',
            context: Sequence[int] | None = None,
            stream: Literal[False] = False,
            raw: bool = False,
            format: Literal['', 'json'] = '',
            images: Sequence[str] | None = None,
            options: OptionsOllama | None = None,
            keep_alive: float | str | None = None
        ) -> Mapping[str, AnyStr]:
        """
        Simula el envío de una solicitud a la API de un modelo de lenguaje para generar texto.

        Args:
            prompt (str): El texto inicial enviado al modelo.
            messages (List[Dict[str, Union[str, List[Dict[str, Union[str, bytes]]]]]]): El historial de mensajes para el modelo.
            max_tokens (int): Número máximo de tokens generados.
            temperature (float): Controla la aleatoriedad de la respuesta.
            top_p (float): Controla el muestreo de "nucleus".
            top_k (Optional[int]): Limita el número de tokens a considerar.

        Returns:
            Dict[str, Union[str, Dict]]: Simulación de una respuesta de la API que contiene el texto generado.
        """
        # Aquí iría el código real para interactuar con el API.
        return ollama.generate()