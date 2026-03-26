from datetime import datetime


class AuroraBrain:
    def analisar_movimento(self, placa: str, status: str) -> str:
        placa = placa.upper().strip()

        if status == "ATIVO":
            return f"[AURORA] Veículo {placa} está em permanência ativa no pátio."
        if status == "FINALIZADO":
            return f"[AURORA] Veículo {placa} concluiu a permanência no estacionamento."

        return f"[AURORA] Status desconhecido para a placa {placa}."

    def detectar_padrao(self, historico: list[dict]) -> str:
        total = len(historico)

        if total == 0:
            return "[AURORA] Nenhum histórico disponível para análise."

        if total > 20:
            return "[AURORA] Fluxo elevado detectado. Recomenda-se atenção operacional reforçada."

        return "[AURORA] Fluxo estável. Operação dentro do padrão esperado."

    def saudacao_tatica(self) -> str:
        return f"[AURORA] Núcleo analítico online em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"