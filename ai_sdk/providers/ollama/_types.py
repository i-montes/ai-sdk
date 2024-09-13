from typing import List, Union, Sequence, Dict, TypedDict

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
    
    
class OptionsOllama(TypedDict, total=False):
    # load time options
    numa: bool
    num_ctx: int
    num_batch: int
    num_gpu: int
    main_gpu: int
    low_vram: bool
    f16_kv: bool
    logits_all: bool
    vocab_only: bool
    use_mmap: bool
    use_mlock: bool
    embedding_only: bool
    num_thread: int

    # runtime options
    num_keep: int
    seed: int
    num_predict: int
    top_k: int
    top_p: float
    tfs_z: float
    typical_p: float
    repeat_last_n: int
    temperature: float
    repeat_penalty: float
    presence_penalty: float
    frequency_penalty: float
    mirostat: int
    mirostat_tau: float
    mirostat_eta: float
    penalize_newline: bool
    stop: Sequence[str]
