import sqlite3
from contextlib import contextmanager

from core.config import settings


def init_db() -> None:
    with sqlite3.connect(settings.DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            telefone TEXT,
            plano TEXT DEFAULT 'ROTATIVO',
            ativo INTEGER DEFAULT 1
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            placa TEXT NOT NULL UNIQUE,
            modelo TEXT,
            cor TEXT,
            tipo TEXT DEFAULT 'CARRO',
            FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placa TEXT NOT NULL,
            entrada_em TEXT NOT NULL,
            saida_em TEXT,
            status TEXT NOT NULL DEFAULT 'ATIVO',
            observacao TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS auditoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento TEXT NOT NULL,
            detalhe TEXT,
            criado_em TEXT NOT NULL
        )
        """)

        conn.commit()


@contextmanager
def get_connection():
    conn = sqlite3.connect(settings.DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()