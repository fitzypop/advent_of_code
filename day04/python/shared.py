import os

import numpy as np

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file() -> tuple[list[int], list[np.matrix]]:
    with open(FILE_NAME) as f:
        draws = list(map(int, f.readline().split(",")))
        boards = [
            np.mat(board.replace("\n", ";"))
            for board in f.read()[1:-1].split("\n\n")  # noqa: E501
        ]

    return (draws, boards)
