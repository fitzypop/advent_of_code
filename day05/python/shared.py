import os
import re

import numpy as np

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file() -> tuple[int, np.ndarray]:
    with open(FILE_NAME) as f:
        lines = f.readlines()
        coords = np.array(
            # get digit strings as tuples using regex groups i.e. (num1, num2, num3, num4)
            [re.match("(\d+),(\d+) -> (\d+),(\d+)", line).groups() for line in lines]
        ).astype(int)

    return (np.max(coords) + 1, coords)


def rrange(start, stop):
    # use regular range, if start is smaller than stop
    # OR get a reversed range if start is greater than stop
    return range(start, stop + 1) if stop >= start else range(start, stop - 1, -1)


# if __name__ == "__main__":
#     with open(FILE_NAME) as f:
#         lines = f.readlines()
#         result = [
#             re.match("(\d+),(\d+) -> (\d+),(\d+)", line).groups() for line in lines
#         ]

#         print(result[:10])
