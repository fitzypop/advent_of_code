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
