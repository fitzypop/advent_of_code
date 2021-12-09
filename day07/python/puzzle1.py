import os
from collections import Counter
from itertools import product

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file() -> Counter:
    with open(FILE_NAME) as f:
        # read first line, remove newline, and split on comma
        # then turn strings into ints, and pass list to Counter
        # to get a Count of all the numbers
        return Counter([int(i) for i in f.read().rstrip().split(",")])
        # Counter -> Keys = Current position, Val = num crabs at that position


def compute(data: Counter) -> int:
    result = (
        Counter()
    )  # Counter -> Keys = New Position, Val = fuel cost for all crabs to move to that position

    upper_bound = max(data.keys())
    # product(iter1, iter2) basically implements a nested for-loop
    for alignment, item in product(range(upper_bound + 1), data.items()):
        fuel_cost = abs(item[0] - alignment) * item[1]
        result.update({alignment: fuel_cost})

    # get the lowest fuel cost
    return min(result.values())


TESTS = [([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 37)]


@pytest.mark.parametrize(("data", "expected"), TESTS)
def test(data, expected):
    assert compute(Counter(data)) == expected


def main() -> int:
    data = read_file()
    result = compute(data)
    print(result)
    return 0


if __name__ == "__main__":
    main()
