import os.path

FILE_NAME = os.path.join(os.path.dirname(__file__), "..", "data.txt")


def read_file() -> list[str]:
    with open(FILE_NAME, "r") as f:
        return f.read().splitlines()


def main() -> int:
    gamma = ""
    epsilon = ""
    data = read_file()
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
    print(f"{n_gamma*n_epsilon=}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
