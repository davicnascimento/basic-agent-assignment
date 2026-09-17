from dataclasses import dataclass
import os
from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str


def load_settings() -> Settings:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("GROQ_API_KEY não está configurada no ficheiro .env")
    return Settings(api_key=api_key, model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"))
