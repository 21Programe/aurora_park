from pydantic import BaseModel, Field


class ClienteCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=120)
    cpf: str = Field(..., min_length=11, max_length=14)
    telefone: str | None = None
    plano: str = "ROTATIVO"


class ClienteResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    telefone: str | None = None
    plano: str
    ativo: int