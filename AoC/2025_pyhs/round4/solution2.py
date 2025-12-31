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


def check_neighbors_fast(data: npt.NDArray, i: int, j: int) -> int:
    sum = 0
    for di, dj in nn_shifts:
        sum += int(data[i + di, j + dj] == "@")
    return int(sum < 4)


if __name__ == "__main__":
    print("Solution2")
    data = readInput()
    n_rows, n_cols = data.shape

    def check_neighbors(data: npt.NDArray, i: int, j: int) -> int:
        coords = map(lambda d: (i + d[0], j + d[1]), nn_shifts)
        coords = filter(lambda d: 0 <= d[0] < n_rows and 0 <= d[1] < n_cols, coords)
        sum = 0
        for row, col in coords:
            sum += int(data[row, col] == "@")
        return int(sum < 4)

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

    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if data[i, j] == ".":
                continue
            count += check_neighbors(data, i, j)

    # count the simple cases (exclude margin)
    # for i in range(1, n_rows - 1):
    # for j in range(1, n_cols - 1):
    # if data[i, j] == ".":
    # continue
    # count += check_neighbors_fast(data, i, j)

    ## count the cases on the margin
    # for row in [0, n_rows - 1]:
    # for col in range(n_cols):
    # if data[row, col] == ".":
    # continue
    # count += check_neighbors(data, row, col)
    #
    # for col in [0, n_cols - 1]:
    # for row in range(1, n_rows - 1):
    # if data[row, col] == ".":
    # continue
    # count += check_neighbors(data, row, col)

    print(f"Result: {count}")
