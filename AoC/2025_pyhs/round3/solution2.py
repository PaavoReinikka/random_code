
import numpy as np

def read_input(file_path):
    result = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            result.append([int(i) for i in line.strip()])
    return np.array(result)

def _get_joltage(x):
    head = x[:-1]
    fst_digit = head.max()
    fst_index = np.where(x == fst_digit)[0][0]
    snd_digit = x[fst_index+1:].max()
    return int(str(fst_digit) + str(snd_digit))


def get_digits(x, n):
    if n==1:
        return str(x.max())
    head = x[:-(n-1)]
    digit = head.max()
    rest = x[np.where(x == digit)[0][0]+1:]
    return str(digit) + get_digits(rest, n-1)

if __name__ == "__main__":
    fname = "input.txt"
    n_digits = 12
    data = read_input(fname)
    voltages = map(lambda x: int(get_digits(x, n_digits)), data)
    print(sum(voltages))
