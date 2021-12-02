import os.path
from queue import Queue

FILE_NAME = os.path.join(os.path.dirname(__file__), "data.txt")


def read_file() -> list[tuple[str, int]]:
    directions: list[tuple[str, int]] = []
    with open(FILE_NAME, "r") as f:
        for line in f.read().splitlines():
            tmp = line.split()
            directions.append((tmp[0], int(tmp[1])))
    return directions


def main() -> int:
    x, y, aim = (0, 0, 0)
    directions = read_file()
    for direc, unit in directions:
        match direc:
            case 'forward':
                x += unit
                y += aim * unit
            case "down":
                aim += unit
            case "up":
                aim -= unit
            case _:
                pass

    print(f"your coordinates are: {(x, y)} your answer is: {x * y}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
