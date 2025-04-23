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
            
    left = np.sort(np.array(left))
    right = np.sort(np.array(right))
    s= 0
    for i in range(len(left)):
        s += np.abs( right[i] - left[i] )
        
    print(f"Total distance: {s}")