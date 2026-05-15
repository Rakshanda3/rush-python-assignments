import sys
from rush import rush


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py x y", file=sys.stderr)
    else:
        try:
            rush(int(sys.argv[1]), int(sys.argv[2]))
        except ValueError:
            print("Invalid size", file=sys.stderr)
