# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:53:35 2024

@author: pr033481

Solutions:
    Day 10:
        - Part1: 329356
        - Part2: 4666278

"""

import numpy as np
import matplotlib.pyplot as plt

def count(x, xs):
    if x==xs[0]:
        return 1 + count(x, xs[1:])
    else:
        return 1



def call(n_iter=40):
    lengths=np.zeros((n_iter,))
    ins="3113322113"
    
    for k in range(n_iter):
        lengths[k]=len(ins)
        i=0
        new_input=""
        
        while i<len(ins):
            if i==len(ins)-1:
                n=1
            else:
                n = count(ins[i],ins[i+1:])
            new_input += str(n) + str(ins[i])
            i += n
            
        ins=new_input
    
    return lengths