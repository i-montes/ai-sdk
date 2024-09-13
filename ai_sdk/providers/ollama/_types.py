from typing import List, Union, Optional, Dict, TypedDict

class OllamaSystemMessage(TypedDict):
    role: str  # Literal["system"] también podría usarse para mayor precisión
    content: str

# Definición de TextPart
class TextPart(TypedDict):
    type: str  # Literal["text"] sería más preciso
    text: str

# Definición de ImagePart
class ImagePart(TypedDict):
    type: str  # Literal["image"]
    image: Union[str, bytes, memoryview]  # Alternativas para representación de imagen

# Definición de OllamaUserMessage
class OllamaUserMessage(TypedDict):
    role: str  # Literal["user"]
    content: List[Union[TextPart, ImagePart]]

# Definición de OllamaAssistantMessage
class OllamaAssistantMessage(TypedDict):
    role: str  # Literal["assistant"]
    content: TextPart