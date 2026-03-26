from database import get_connection
from security.audit import registrar_evento


class VeiculoService:
    @staticmethod
    def criar(data: dict) -> dict:
        placa = data["placa"].upper().strip()

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO veiculos (cliente_id, placa, modelo, cor, tipo)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    data.get("cliente_id"),
                    placa,
                    data.get("modelo"),
                    data.get("cor"),
                    data.get("tipo", "CARRO")
                )
            )
            conn.commit()

            veiculo_id = cursor.lastrowid
            registrar_evento("VEICULO_CRIADO", f"Veículo ID {veiculo_id} / placa {placa} cadastrado.")

            return {
                "id": veiculo_id,
                "cliente_id": data.get("cliente_id"),
                "placa": placa,
                "modelo": data.get("modelo"),
                "cor": data.get("cor"),
                "tipo": data.get("tipo", "CARRO")
            }

    @staticmethod
    def listar() -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute("SELECT * FROM veiculos ORDER BY id DESC").fetchall()
            return [dict(row) for row in rows]