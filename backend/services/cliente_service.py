from database import get_connection
from security.audit import registrar_evento


class ClienteService:
    @staticmethod
    def criar(data: dict) -> dict:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO clientes (nome, cpf, telefone, plano)
                VALUES (?, ?, ?, ?)
                """,
                (
                    data["nome"],
                    data["cpf"],
                    data.get("telefone"),
                    data.get("plano", "ROTATIVO")
                )
            )
            conn.commit()

            cliente_id = cursor.lastrowid
            registrar_evento("CLIENTE_CRIADO", f"Cliente ID {cliente_id} cadastrado.")

            return {
                "id": cliente_id,
                "nome": data["nome"],
                "cpf": data["cpf"],
                "telefone": data.get("telefone"),
                "plano": data.get("plano", "ROTATIVO"),
                "ativo": 1
            }

    @staticmethod
    def listar() -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute("SELECT * FROM clientes ORDER BY id DESC").fetchall()
            return [dict(row) for row in rows]