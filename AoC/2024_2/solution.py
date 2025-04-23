# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:02:26 2025

@author: pr033481

- Day 2:
  - Part 1: 282
  - Part 2: 349
  
"""
import numpy as np
import copy

def toInts(s):
    items = s.split(" ")
    return [int(item) for item in items]

def safe(arr):
    diff = np.diff(arr)
    if np.all(np.sort(arr)==arr):
        return np.all(diff<=3) and np.all(diff>=1)

    elif np.all(np.sort(arr)==arr[::-1]):
        return np.all(diff>=-3) and np.all(diff<=-1)        
    return False
        

    
with open("input.txt") as f:
    lines = f.readlines()
    
data = [toInts(elem.strip()) for elem in lines]

n_safe = np.sum([safe(elem) for elem in data])

print(f"Number of safe: {n_safe}")
