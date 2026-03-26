from datetime import datetime

from database import get_connection


def registrar_evento(evento: str, detalhe: str = "") -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO auditoria (evento, detalhe, criado_em)
            VALUES (?, ?, ?)
            """,
            (evento, detalhe, datetime.now().isoformat())
        )
        conn.commit()