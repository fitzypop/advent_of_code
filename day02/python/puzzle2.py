import os.path

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def process_data_file() -> list[tuple[str, int]]:
    data: list[tuple[str, int]] = []
    with open(FILE_NAME, "r") as f:
        return parse(f.read().splitlines())

def parse(lines: list[str]) -> list[tuple[str, int]]:
    data = []
    for line in lines:
        cmd, n_s = line.split()
        data.append((cmd, int(n_s)))

    return data

def compute(data: list[tuple[str, int]]) -> int:
    x = y = aim = 0
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
    return x * y


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
        900,
    )
]


@pytest.mark.parametrize(("input_data", "expected"), TESTS)
def test(input_data, expected):
    assert compute(parse(input_data)) == expected

def main() -> int:
    data = process_data_file()
    result = compute(data)
    print(f"your answer is: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
