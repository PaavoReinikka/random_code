import numpy as np
import numpy.typing as npt

nn_shifts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def readInput():
    lines = []
    with open("input.txt", "r") as f:
        data = f.readlines()

    for line in data:
        lines.append([c for c in line.strip()])

    n_cols = sum((1 for i in lines[0]))
    n_rows = len(lines)
    print(f"{n_cols} columns and {n_rows} rows")

    return np.asarray(lines, dtype=str)


if __name__ == "__main__":
    print("Solution2")
    data = readInput()
    n_rows, n_cols = data.shape

    def check_and_paint(data: npt.NDArray, i: int, j: int) -> int:
        coords = map(lambda d: (i + d[0], j + d[1]), nn_shifts)
        coords = filter(lambda d: 0 <= d[0] < n_rows and 0 <= d[1] < n_cols, coords)
        sum = 0
        for row, col in coords:
            sum += int(data[row, col] == "@")
        if sum < 4:
            data[i, j] = "x"
            return 1
        return 0

    def runner() -> int:
        count = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if data[i, j] in [".", "x"]:
                    continue
                count += check_and_paint(data, i, j)
        return count

    count = 0
    while (previous := runner()) > 0:
        count += previous

    print(f"Result: {count}")
