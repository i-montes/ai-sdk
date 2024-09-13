from ai_sdk.providers import OllamaProvider

ollama = OllamaProvider("llama3.1")

res = ollama.generate_text("¿Qué es el clima?")

print(res)