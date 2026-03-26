from pydantic import BaseModel, Field


class EntradaCreate(BaseModel):
    placa: str = Field(..., min_length=7, max_length=10)
    observacao: str | None = None


class SaidaCreate(BaseModel):
    placa: str = Field(..., min_length=7, max_length=10)


class MovimentacaoResponse(BaseModel):
    id: int
    placa: str
    entrada_em: str
    saida_em: str | None = None
    status: str
    observacao: str | None = None