import os
from collections import Counter

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "data.txt")


def read_file() -> list[int]:
    with open(FILE_NAME) as f:
        line = f.read().splitlines()[0]
        return list(map(int, line.split(",")))


def compute(data: list[int]) -> int:
    numbers = Counter(data)

    for i in range(256):
        numbers2 = Counter({8: numbers[0], 6: numbers[0]})
        numbers2.update({k - 1: v for k, v in numbers.items() if k > 0})
        numbers = numbers2
    return sum(numbers.values())


INPUT_DATA = [3, 4, 3, 1, 2]
EXPECTED = 26984457539


@pytest.mark.parametrize(
    ("input_data", "expected"),
    ((INPUT_DATA, EXPECTED),),
)
def test(input_data, expected):
    assert compute(input_data) == expected


def main() -> int:
    result = compute(read_file())
    print(f"Answer for day 6 puzzle 1 is: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
