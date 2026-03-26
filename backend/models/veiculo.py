from pydantic import BaseModel, Field


class VeiculoCreate(BaseModel):
    cliente_id: int | None = None
    placa: str = Field(..., min_length=7, max_length=10)
    modelo: str | None = None
    cor: str | None = None
    tipo: str = "CARRO"


class VeiculoResponse(BaseModel):
    id: int
    cliente_id: int | None = None
    placa: str
    modelo: str | None = None
    cor: str | None = None
    tipo: str