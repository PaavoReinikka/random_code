# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:13:19 2025

@author: pr033481


- Day 1:
  - Part 1: 2086478
  - Part 2: 24941624
  
"""
import numpy as np

with open("input.txt") as f:
    lines = f.readlines()
    
left = np.zeros((1000,))
right = np.zeros((1000,))

for i, line in enumerate(lines):
    pair = line.strip().split("   ")
    left[i] = pair[0]
    right[i] = pair[1]


left  = np.sort(left)
right = np.sort(right)

dist = np.sum(np.abs(left - right))
print(f"Distances: {dist}")

occurences = np.array([np.sum(elem==right) for elem in left])
sim = np.sum(left * occurences)
print(f"similarity: {sim}")
