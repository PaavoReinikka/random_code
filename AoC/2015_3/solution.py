# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:53:35 2024

@author: pr033481

Solutions:
    Day 10:
        - Part1: 329356
        - Part2: 4666278

"""

def count(x, xs):
    if len(xs)==1:
        return int(x==xs)
    elif x==xs[0]:
        return 1 + count(x, xs[1:])
    else:
        return 1



ins="3113322113"
i=0
new_input=""

while i<len(ins):
    
    if i==len(ins)-1:
        n=1
    else:
        n=count(ins[i],ins[i+1:])
    
    new_input+=str(n)
    new_input+=str(ins[i])
    print(new_input)
    i+=n
    
new_input
