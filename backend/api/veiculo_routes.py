from fastapi import APIRouter, HTTPException

from models.veiculo import VeiculoCreate
from services.veiculo_service import VeiculoService

router = APIRouter(prefix="/veiculos", tags=["Veículos"])


@router.post("/")
def criar_veiculo(payload: VeiculoCreate):
    try:
        return VeiculoService.criar(payload.model_dump())
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/")
def listar_veiculos():
    return VeiculoService.listar()