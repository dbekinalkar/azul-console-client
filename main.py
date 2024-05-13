import argparse
import asyncio
import websockets
from websockets.sync.client import connect, ClientConnection
import threading

def listen_server(ws: ClientConnection) -> None:
    message: str
    for message in ws:
        print(f"Received from server: {message}")

def send_messages(ws: ClientConnection) -> None:
    while True:
        message: str = input()
        if message == "quit":
            break
        
        ws.send(message)

def parse_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Client to connect to Azul server.")
    parser.add_argument("host", nargs='?', type=str, default="localhost", help="Azul server host (default: localhost)")
    parser.add_argument("port", nargs='?', type=int, default=3000, help="Port number (default: 3000)")
    args: argparse.Namespace = parser.parse_args()
    return args

async def main() -> None:
    args: argparse.Namespace = parse_args()

    uri: str = f"ws://{args.host}:{args.port}"

    print(f'Connecting to {uri}')

    ws: ClientConnection
    with connect(uri) as ws:
        listener: threading.Thread = threading.Thread(target=listen_server, args=([ws]), name="Listener")

        listener.start()

        send_messages(ws)
        ws.close()

        listener.join()

    print("Connection closed")


if __name__ == '__main__':
    asyncio.run(main())