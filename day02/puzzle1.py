import os.path

FILE_NAME = os.path.join(os.path.dirname(__file__), "data.txt")


def process_data_file() -> dict[str, int]:
    directions = {"up": 0, "down": 0, "forward": 0}
    with open(FILE_NAME, "r") as f:
        for line in f.read().splitlines():
            tmp = line.split()
            directions[tmp[0]] += int(tmp[1])

    return directions


def main() -> int:
    data = process_data_file()
    x = data["forward"]
    y = data["down"] - data["up"]
    final = x * y
    print(f"your coordinates are: {(x, y)}")
    print(f"your answer is: {final}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
