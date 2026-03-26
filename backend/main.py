from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.cliente_routes import router as cliente_router
from api.veiculo_routes import router as veiculo_router
from api.movimentacao_routes import router as movimentacao_router
from core.config import settings
from database import init_db

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
def home():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "online"
    }


app.include_router(cliente_router)
app.include_router(veiculo_router)
app.include_router(movimentacao_router)