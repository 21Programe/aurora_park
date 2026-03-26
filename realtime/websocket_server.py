import asyncio
import websockets
import sys
import os

# Ajuste para permitir que o Python encontre a pasta 'ai'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai.aurora_brain import AuroraBrain

# Inicializa o núcleo da IA
aurora = AuroraBrain()
clientes_conectados = set()

async def handler(websocket):
    clientes_conectados.add(websocket)
    print(f"[REALTIME] Nova conexão estabelecida. Total: {len(clientes_conectados)}")
    
    # Assim que conecta, a Aurora envia sua Saudação Tática
    saudacao = aurora.saudacao_tatica()
    await websocket.send(saudacao)

    try:
        async for mensagem in websocket:
            # A Aurora analisa o que você escreveu
            analise = f"[AURORA] Feedback: Recebi seu sinal -> '{mensagem}'"
            await websocket.send(analise)
            
    except websockets.exceptions.ConnectionClosed:
        print("[REALTIME] Um cliente desconectou.")
    finally:
        clientes_conectados.remove(websocket)

async def main():
    print("-----------------------------------------")
    print("🚀 AURORA REALTIME CORE: ONLINE")
    print("📍 Endereço: ws://127.0.0.1:8765")
    print("-----------------------------------------")
    
    async with websockets.serve(handler, "127.0.0.1", 8765):
        await asyncio.Future()  # Mantém o servidor rodando para sempre

if __name__ == "__main__":
    asyncio.run(main())