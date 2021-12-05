import os
import re

import numpy as np

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file() -> tuple[int, np.ndarray]:
    with open(FILE_NAME) as f:
        lines = f.readlines()
        coords = np.array(
            [re.match("(\d+),(\d+) -> (\d+),(\d+)", line).groups() for line in lines]
        ).astype(int)

    return (np.max(coords) + 1, coords)


def rrange(start, stop):
    return range(start, stop + 1) if stop >= start else range(start, stop - 1, -1)


def main() -> int:
    size, coords = read_file()
    grid = np.zeros((size, size))
    hv = coords[(coords[:, 0] == coords[:, 2]) + (coords[:, 1] == coords[:, 3])]
    for x1, y1, x2, y2 in hv:
        grid[rrange(y1, y2), rrange(x1, x2)] += 1
    result = (grid >= 2).sum()
    print(f"Answer for day 5 / puzzle 1: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
