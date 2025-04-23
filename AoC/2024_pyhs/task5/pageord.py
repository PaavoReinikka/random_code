# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:45:50 2024

@author: paavo
"""
from functools import cmp_to_key

pairs = []
values = []
with open("input.txt") as f:
    lines = f.readlines()
    flag=True
    for line in lines:
        if line=="\n":
            flag=False
            continue
        if flag:
            a, b = line.strip().split("|")
            pairs.append((a,b))
        else:
            vals = line.strip().split(",")
            values.append(vals)

def getGreaters(x):
    return [elem[1] for elem in pairs if elem[0]==x]
def getLessers(x):
    return [elem[0] for elem in pairs if elem[1]==x]

def outOfOrder(left, right):
    if right in getLessers(left):
        return True
    if left in getGreaters(right):
        return True
    return False

def testOrdering(xs):
    
    for i, elem in enumerate(xs):
        for j in range(i+1, len(xs)):
            if outOfOrder(elem, xs[j]):
                return False
    return True

def pick_middle(xs):
    return int(xs[len(xs)//2])

#inplace
def swap(xs, ind):
    tmp=xs[:][ind]
    xs[ind]=xs[:][ind+1]
    xs[ind+1]=tmp
    return xs

"""
acc=0
for vals in values:
    if testOrdering(vals):
        acc+=pick_middle(vals)
        
print(acc)
"""


def ordering(x,y):
    if any([elem[0]==x and elem[1]==y for elem in pairs]):
        return -1
    if any([elem[0]==y and elem[1]==x for elem in pairs]):
        return 1
    return 0
   
acc=0
for vals in values:
    if testOrdering(vals):
        continue
    else:
        sorted_vals = sorted(vals,key=cmp_to_key(ordering))
        if testOrdering(sorted_vals):
            acc+=pick_middle(sorted_vals)
        
        
print(acc)

    


