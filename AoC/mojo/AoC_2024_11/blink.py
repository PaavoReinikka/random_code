import sys
import time
import multiprocessing
from functools import partial

def blinkOne(s):
    if s=="0":
        return "1"
    elif len(s)%2==0:
        return str(int(s[:len(s)//2])) + " " + str(int(s[len(s)//2:]))
    else:
        return str(2024*int(s))

def blink(ss):
    acc=""
    for s in ss.split():
        acc+=blinkOne(s) + " "
    return acc[:-1]

def blink_ntimes(data, n=25):
    for i in range(n):
        data=blink(data)
    return len(data.split(" "))


def main(n_times):

    try:
        n_times=int(n_times)
        print(f"blinking {n_times} times")
    except ValueError:
        print("Need an integer as the first commandline argument,")
        print("defaulting to 25 blinks")

    data = "890 0 1 935698 68001 3441397 7221 27"
    print(f"Using {data} as input.")

    """
    start = time.time()
    acc=0
    for s in data.split(" "):
        acc+=blink_ntimes(s, n_times)
    total = time.time() - start
    print(f"The number of stones after {n_times} blinks is {acc}")
    print(f"total time: {total}")
    """

    pool = multiprocessing.Pool(processes=8)
    start=time.time()
    result = pool.map(partial(blink_ntimes, n=n_times), data.split(" "))
    total=time.time()-start
    
    print(f"The number of stones after {n_times} blinks: {sum(result)}")
    print(f"Total time: {total}")


if __name__=="__main__":
    main(sys.argv[1])


