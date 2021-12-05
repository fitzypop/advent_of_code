import os
from enum import Enum

FILE_NAME = os.path.join(os.path.dirname(__file__), "data.txt")


def read_file() -> list[str]:
    with open(FILE_NAME, "r") as f:
        return f.read().splitlines()


class Criteria(Enum):
    LEAST = 0
    MOST = 1


def main() -> int:
    data = read_file()

    num1 = int(reduce(data, Criteria.MOST), 2)
    num2 = int(reduce(data, Criteria.LEAST), 2)
    print(f"Puzzle 2 answer is: {num1 * num2}")
    return 0


criteria = {
    Criteria.MOST: lambda x, y: x if len(x) > len(y) else y,
    Criteria.LEAST: lambda x, y: x if len(x) < len(y) else y,
}


def reduce(data: list[str], m_criteria: Criteria, i_pos: int = 0):
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


if __name__ == "__main__":
    main()
