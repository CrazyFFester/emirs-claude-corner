import argparse
import shutil


def step(cells: list[int], rule: int) -> list[int]:
    width = len(cells)
    return [
        (rule >> (cells[(i - 1) % width] << 2 | cells[i] << 1 | cells[(i + 1) % width])) & 1
        for i in range(width)
    ]


def center_column_bits(rule: int, count: int) -> str:
    width = 2 * count + 1
    cells = [0] * width
    cells[count] = 1
    bits: list[str] = []
    for _ in range(count):
        bits.append(str(cells[count]))
        cells = step(cells, rule)
    return "".join(bits)


def main() -> None:
    parser = argparse.ArgumentParser(description="Elementary cellular automaton, one seed cell.")
    parser.add_argument("--rule", type=int, default=30, choices=range(256), metavar="0-255")
    parser.add_argument("--generations", type=int, default=32)
    parser.add_argument("--width", type=int, default=min(shutil.get_terminal_size().columns, 101))
    parser.add_argument("--center", action="store_true", help="print the center column as bits instead")
    args = parser.parse_args()

    if args.center:
        print(center_column_bits(args.rule, args.generations))
        return

    cells = [0] * args.width
    cells[args.width // 2] = 1
    for _ in range(args.generations):
        print("".join("█" if alive else " " for alive in cells))
        cells = step(cells, args.rule)


if __name__ == "__main__":
    main()
