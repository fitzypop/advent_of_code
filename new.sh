#!/usr/bin/env bash

if [ -z "$1" ]; then
    echo -e "Error: First argument not found!\nPlease enter new directory name"
    echo -e "\n - new.sh - Script for Advent of Code. Make a new dir step up for an aoc day."
    echo -e "\nusage: ./new.sh dir_name <optional: python version default=3.10>"
    exit 1
fi

DIR_NAME=$1

mkdir -p "$DIR_NAME"
cd "$DIR_NAME"
touch data.txt
touch README.md

mkdir python
cd python
PYTHON_CODE=$(cat <<EOF
import os

import pytest

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file():
    with open(FILE_NAME) as f:
        pass


def compute(data):
    pass


TESTS = [([], 0)]


@pytest.mark.parametrize(("data", "expected"), TESTS)
def test(data, expected):
    assert compute(data) == expected


def main() -> int:
    data = read_file()
    result = compute(data)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
EOF
)

echo "$PYTHON_CODE" > puzzle1.py
echo "$PYTHON_CODE" > puzzle2.py
