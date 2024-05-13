import argparse
import asyncio
import websockets

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

    ws: websockets.WebSocketClientProtocol
    async with websockets.connect(uri) as ws:
        while True:
            message: str = input()
            if message == "quit":
                break
                
            await ws.send(message)

            receipt: str = await ws.recv()

            print(f"Received from server: {receipt}")
            

    print("Connection closed")


if __name__ == '__main__':
    asyncio.run(main())