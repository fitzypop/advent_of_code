import os.path

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file() -> list[str]:
    with open(FILE_NAME, "r") as f:
        return f.read().splitlines()


def compute(data: list[str]) -> int:
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        zero_count = 0
        one_count = 0
        for item in data:
            if item[i] == "0":
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    n_gamma = int(gamma, 2)
    n_epsilon = int(epsilon, 2)
    return n_gamma * n_epsilon


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
        198,
    )
]


@pytest.mark.parametrize(("input_data", "expected"), TESTS)
def test(input_data, expected):
    assert compute(input_data) == expected


def main() -> int:
    data = read_file()
    print(f"{compute(data)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
