import argparse

def parse_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Client to connect to Azul server.")
    parser.add_argument("host", nargs='?', type=str, default="localhost", help="Azul server host (default: localhost)")
    parser.add_argument("port", nargs='?', type=int, default=3000, help="Port number (default: 3000)")
    args: argparse.Namespace = parser.parse_args()
    return args

def main() -> None:
    args: argparse.Namespace = parse_args()

    print(f'Connecting to {args.host}:{args.port}')

if __name__ == '__main__':
    main()