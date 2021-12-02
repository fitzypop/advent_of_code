from shared import calculate_depth_increases, read_file


def main() -> int:
    depths = read_file()
    print(f"number of depth measurements: {len(depths)}")

    increased_count = calculate_depth_increases(depths)
    print(f"number of increased depths: {increased_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
