
import numpy as np

def read_input(file_path):
    result = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            result.append([int(i) for i in line.strip()])
    return np.array(result)

def get_joltage(x):
    head = x[:-1]
    fst_digit = head.max()
    fst_index = np.where(x == fst_digit)[0][0]
    snd_digit = x[fst_index+1:].max()
    return int(str(fst_digit) + str(snd_digit))
    

if __name__ == "__main__":
    fname = "input.txt"
    data = read_input(fname)
    voltages = map(get_joltage, data)
    print(sum(voltages))
