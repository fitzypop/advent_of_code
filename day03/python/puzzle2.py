import os
from enum import Enum

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


class Criteria(Enum):
    LEAST = 0
    MOST = 1


criteria = {
    Criteria.MOST: lambda x, y: x if len(x) > len(y) else y,
    Criteria.LEAST: lambda x, y: x if len(x) < len(y) else y,
}


def read_file() -> list[str]:
    with open(FILE_NAME, "r") as f:
        return f.read().splitlines()


def reduce(data: list[str], m_criteria: Criteria, i_pos: int = 0) -> str:
    if len(data) == 1:
        return data[0]

    zeros = []
    ones = []
    for item in data:
        if item[i_pos] == "0":
            zeros.append(item)
        else:
            ones.append(item)

    next_data = []

    if len(zeros) == len(ones):
        next_data = ones if m_criteria is Criteria.MOST else zeros
    else:
        next_data = criteria[m_criteria](zeros, ones)

    return reduce(next_data, m_criteria, i_pos + 1)


def compute(data: list[str]) -> int:
    num1 = int(reduce(data, Criteria.MOST), 2)
    num2 = int(reduce(data, Criteria.LEAST), 2)
    return num1 * num2


TESTS = [
    (
        [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ],
        230,
    )
]


@pytest.mark.parametrize(("input_data", "expected"), TESTS)
def test(input_data, expected):
    assert compute(input_data) == expected


def main() -> int:
    data = read_file()
    result = compute(data)
    print(f"Puzzle 2 answer is: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
