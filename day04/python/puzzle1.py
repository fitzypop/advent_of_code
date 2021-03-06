import os
from itertools import product

import numpy as np

from shared import read_file


def compute(draws, bo)

def main() -> int:
    draws, boards = read_file()

    result = -1
    for draw, masked_board in product(
        draws, [np.ma.masked_array(board) for board in boards]
    ):
        # np special operates
        # board.data is the entire array
        # == will check if the val in spot in the matrix
        # |= will take the true or false value from the check
        # and add it to the mask matrix
        masked_board.mask |= masked_board.data == draw
        if np.any(masked_board.mask.sum(0) == 5) or np.any(
            masked_board.mask.sum(1) == 5
        ):
            result = masked_board.sum() * draw
            break

    print(f"Answer for day 4/puzzle 1 : {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
