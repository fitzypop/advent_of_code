import os.path

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file() -> list[int]:
    with open(FILE_NAME) as f:
        return [int(line) for line in f.read().splitlines()]


TESTS = [
    ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
    ([607, 618, 618, 617, 647, 716, 769, 792], 5),
]


@pytest.mark.parametrize(("input_data", "expected"), TESTS)
def test(input_data, expected):
    assert calculate_depth_increases(input_data) == expected


def calculate_depth_increases(depths: list[int] = None) -> int:
    if not depths:
        return 0
    return sum(depths[i] > depths[i - 1] for i in range(1, len(depths)))
