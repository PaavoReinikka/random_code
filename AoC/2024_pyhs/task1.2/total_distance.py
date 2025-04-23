import numpy as np

if __name__ == '__main__':
    left = []
    right = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            split_line = line.split()
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))
            
    left = np.array(left)
    right = np.array(right)
    
    nz = lambda x: np.count_nonzero(right == x)
    nz_vec = np.vectorize(nz)
    print(np.sum(left*nz_vec(left)))