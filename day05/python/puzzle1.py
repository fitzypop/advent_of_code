import numpy as np

from shared import read_file, rrange


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
