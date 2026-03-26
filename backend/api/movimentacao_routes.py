from fastapi import APIRouter, HTTPException

from models.movimentacao import EntradaCreate, SaidaCreate
from services.movimentacao_service import MovimentacaoService

router = APIRouter(prefix="/movimentacoes", tags=["Movimentações"])


@router.post("/entrada")
def registrar_entrada(payload: EntradaCreate):
    try:
        return MovimentacaoService.registrar_entrada(payload.model_dump())
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.post("/saida")
def registrar_saida(payload: SaidaCreate):
    try:
        return MovimentacaoService.registrar_saida(payload.placa)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/")
def listar_movimentacoes():
    return MovimentacaoService.listar()


@router.get("/dashboard")
def obter_dashboard():
    return MovimentacaoService.dashboard()