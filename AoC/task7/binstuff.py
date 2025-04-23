import math
import re

def gen_bins(n):
    bin_arr = range(0, int(math.pow(2,n)))
    bin_arr = [bin(i)[2:] for i in bin_arr]

    max_len = len(max(bin_arr, key=len))
    return [i.zfill(max_len) for i in bin_arr]


def zipWith(values, bins, check_value):
    bins += "#"# end mark
    acc = ""

    for i, elem in enumerate(values):
        if bins[i]=="0":
            op="+"
        elif bins[i]=="1":
            op="*"
        else:
            op=""
        acc += elem
        acc += op

    value = eval(acc)
    truth = value == check_value
    if truth:
        print(f"{acc}={value}={check_value}")
    return truth

def accumulator(value, elems):
    n = len(elems)-1
    bins = gen_bins(n)

    for  b in bins:
        if zipWith(elems, b, value):
            return value

    return 0

def parse(s):
    res = re.findall("[0-9]+",s)
    value = int(res[0])
    elems = res[1:]
    return value, elems

if __name__=="__main__":

    acc=0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            value, elems = parse(line.strip())
            acc += accumulator(value, elems)

    print(f"final result: {acc}")
