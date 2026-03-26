from pathlib import Path


class Settings:
    APP_NAME = "Aurora Park System"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "Sistema inteligente de gestão de estacionamento com IA, monitoramento e operação em tempo real."

    BASE_DIR = Path(__file__).resolve().parents[2]
    DB_PATH = BASE_DIR / "backend" / "aurora_park.db"


settings = Settings()