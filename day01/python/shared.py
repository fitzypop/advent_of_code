import os.path

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file() -> list[int]:
    with open(FILE_NAME) as f:
        return [int(line) for line in f.read().splitlines()]


def calculate_depth_increases(depths: list[int] = None) -> int:
    if not depths:
        return 0
    return sum(depths[i] > depths[i - 1] for i in range(1, len(depths)))
