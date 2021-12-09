import os.path
from collections import defaultdict

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def process_data_file() -> dict[str, int]:
    with open(FILE_NAME, "r") as f:
        lines = f.read().splitlines()
        return parse(lines)


def parse(lines: list[str]) -> dict[str, int]:
    directions = defaultdict(int)
    combos = [line.split() for line in lines]
    for command, num_str in combos:
        directions[command] += int(num_str)

    return directions


TESTS = [
    (
        [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2",
        ],
        150,
    )
]


@pytest.mark.parametrize(("input_data", "expected"), TESTS)
def test(input_data, expected):
    assert compute(parse(input_data)) == expected


def compute(data: dict[str, int]) -> int:
    return data["forward"] * (data["down"] - data["up"])


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
