from groq import Groq
from src.config import Settings
from src.prompt import SYSTEM_PROMPT


def classify_message(settings: Settings, message: str) -> dict:
    """Envia uma mensagem ao modelo e devolve o JSON produzido."""
    # TODO: implementar a chamada chat.completions.create com response_format JSON.
    raise NotImplementedError("Implementar a chamada ao Groq")
