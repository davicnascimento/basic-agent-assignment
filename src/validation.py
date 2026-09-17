from typing import Literal
from pydantic import BaseModel, ConfigDict, field_validator


class TriageResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    category: Literal["cartao", "transferencia", "conta", "acesso_app", "possivel_fraude", "desconhecida"]
    urgency: Literal["baixa", "media", "alta"]
    response: str

    @field_validator("response")
    @classmethod
    def response_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("response não pode estar vazia")
        return value.strip()


def validate_result(result: dict) -> TriageResult:
    return TriageResult.model_validate(result)
