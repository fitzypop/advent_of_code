import os.path

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def process_data_file() -> list[tuple[str, int]]:
    data: list[tuple[str, int]] = []
    with open(FILE_NAME, "r") as f:
        for cmd, n_s in [line.split() for line in f.read().splitlines()]:
            data.append((cmd, int(n_s)))
    return data


def main() -> int:
    x = y = aim = 0
    data = process_data_file()
    for direction, unit in data:
        match direction:
            case 'forward':
                x += unit
                y += aim * unit
            case "down":
                aim += unit
            case "up":
                aim -= unit
            case _:
                pass

    final = x * y
    print(f"your coordinates are: {(x, y)}")
    print(f"your answer is: {final}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
