from shared import calculate_depth_increases, read_file


def chunk_depths(depths: list[int]) -> list[int]:
    return [depths[i] + depths[i + 1] + depths[i + 2] for i in range(len(depths) - 2)]


def main() -> int:
    depths = read_file()
    print(f"number of depth measurements: {len(depths)}")

    spreads = chunk_depths(depths)
    print(f"Number of depth windows: {len(spreads)}")

    increased_count = calculate_depth_increases(spreads)
    print(f"number of increased depths: {increased_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
