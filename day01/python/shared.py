import os.path

DEFAULT_FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file(file_name: str = None) -> list[int]:
    if not file_name:
        file_name = DEFAULT_FILE_NAME

    with open(file_name, "r") as f:
        depths = [int(line) for line in f.read().splitlines()]

    return depths


def calculate_depth_increases(depths: list[int] = None) -> int:
    if not depths:
        return 0
    return sum(depths[i] > depths[i - 1] for i in range(1, len(depths)))
