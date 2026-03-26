from datetime import datetime

from database import get_connection
from security.audit import registrar_evento


class MovimentacaoService:
    @staticmethod
    def registrar_entrada(data: dict) -> dict:
        placa = data["placa"].upper().strip()

        with get_connection() as conn:
            cursor = conn.cursor()

            aberto = cursor.execute(
                """
                SELECT * FROM movimentacoes
                WHERE placa = ? AND status = 'ATIVO'
                """,
                (placa,)
            ).fetchone()

            if aberto:
                raise ValueError(f"Já existe uma entrada ativa para a placa {placa}.")

            entrada_em = datetime.now().isoformat()

            cursor.execute(
                """
                INSERT INTO movimentacoes (placa, entrada_em, status, observacao)
                VALUES (?, ?, 'ATIVO', ?)
                """,
                (placa, entrada_em, data.get("observacao"))
            )
            conn.commit()

            movimento_id = cursor.lastrowid
            registrar_evento("ENTRADA_REGISTRADA", f"Movimentação ID {movimento_id} / placa {placa}")

            return {
                "id": movimento_id,
                "placa": placa,
                "entrada_em": entrada_em,
                "saida_em": None,
                "status": "ATIVO",
                "observacao": data.get("observacao")
            }

    @staticmethod
    def registrar_saida(placa: str) -> dict:
        placa = placa.upper().strip()

        with get_connection() as conn:
            cursor = conn.cursor()

            row = cursor.execute(
                """
                SELECT * FROM movimentacoes
                WHERE placa = ? AND status = 'ATIVO'
                ORDER BY id DESC
                LIMIT 1
                """,
                (placa,)
            ).fetchone()

            if not row:
                raise ValueError(f"Não há movimentação ativa para a placa {placa}.")

            saida_em = datetime.now().isoformat()

            cursor.execute(
                """
                UPDATE movimentacoes
                SET saida_em = ?, status = 'FINALIZADO'
                WHERE id = ?
                """,
                (saida_em, row["id"])
            )
            conn.commit()

            registrar_evento("SAIDA_REGISTRADA", f"Movimentação ID {row['id']} / placa {placa}")

            return {
                "id": row["id"],
                "placa": placa,
                "entrada_em": row["entrada_em"],
                "saida_em": saida_em,
                "status": "FINALIZADO",
                "observacao": row["observacao"]
            }

    @staticmethod
    def listar() -> list[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            rows = cursor.execute(
                "SELECT * FROM movimentacoes ORDER BY id DESC"
            ).fetchall()
            return [dict(row) for row in rows]

    @staticmethod
    def dashboard() -> dict:
        with get_connection() as conn:
            cursor = conn.cursor()

            ativos = cursor.execute(
                "SELECT COUNT(*) AS total FROM movimentacoes WHERE status = 'ATIVO'"
            ).fetchone()["total"]

            finalizados = cursor.execute(
                "SELECT COUNT(*) AS total FROM movimentacoes WHERE status = 'FINALIZADO'"
            ).fetchone()["total"]

            clientes = cursor.execute(
                "SELECT COUNT(*) AS total FROM clientes"
            ).fetchone()["total"]

            veiculos = cursor.execute(
                "SELECT COUNT(*) AS total FROM veiculos"
            ).fetchone()["total"]

            return {
                "clientes": clientes,
                "veiculos": veiculos,
                "movimentacoes_ativas": ativos,
                "movimentacoes_finalizadas": finalizados
            }