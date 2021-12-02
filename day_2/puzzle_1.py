import os.path

FILE_NAME = os.path.join(os.path.dirname(__file__), "data.txt")


def read_file() -> dict[str, int]:
    directions = {"up": 0, "down": 0, "forward": 0}
    with open(FILE_NAME, "r") as f:
        for line in f.read().splitlines():
            tmp = line.split()
            try:
                directions[tmp[0]] += int(tmp[1])
            except:
                pass

    return directions


def main() -> int:
    directions = read_file()
    x = directions["forward"]
    y = directions["down"] - directions["up"]

    print(f"your depths coordinates are: {(x, y)}")
    print(f"The product is: {x * y}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
