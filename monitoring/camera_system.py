import time
from datetime import datetime


class CameraSystem:
    def __init__(self):
        self.ativo = False

    def iniciar_monitoramento(self):
        self.ativo = True
        print("[MONITORAMENTO] Sistema de vigilância iniciado.")

        while self.ativo:
            evento = {
                "timestamp": datetime.now().isoformat(),
                "camera": "CAM-01",
                "status": "OPERANDO",
                "mensagem": "Monitoramento contínuo do pátio."
            }
            print(evento)
            time.sleep(5)

    def parar_monitoramento(self):
        self.ativo = False
        print("[MONITORAMENTO] Sistema de vigilância finalizado.")