import os

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "data.txt")


def read_file() -> list[int]:
    with open(FILE_NAME) as f:
        line = f.read().splitlines()[0]
        return list(map(int, line.split(",")))


def compute(data: list[int], n: int = 0, limit: int = 80) -> int:
    if n >= limit:
        return len(data)

    new_data = [None] * len(data)
    for i, val in enumerate(data):
        val -= 1
        if val < 0:
            val = 6
            new_data.append(8)
        new_data[i] = val

    return compute(new_data, n + 1, limit)


INPUT_DATA = [3, 4, 3, 1, 2]
EXPECTED = 5934


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
