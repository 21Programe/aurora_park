from fastapi import APIRouter, HTTPException

from models.cliente import ClienteCreate
from services.cliente_service import ClienteService

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("/")
def criar_cliente(payload: ClienteCreate):
    try:
        return ClienteService.criar(payload.model_dump())
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/")
def listar_clientes():
    return ClienteService.listar()