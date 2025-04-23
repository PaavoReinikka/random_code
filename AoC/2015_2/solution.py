# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:05:06 2024

@author: pr033481

Day 2:
    - Part1: 1606483
    - Part2: 3842356
    
"""


"""

IF THE DAT AIS IN input.txt, run this,
otherwise just use the input_list object

import re
input_lista = []
pattern = r'(\w+\d+)'
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        input_lista.append(re.findall(pattern, line)[0])
"""

data = []
for elem in input_lista:
    [l,w,h] = elem.split("x")
    l, w, h =int(l), int(w), int(h)
    data.append([l,w,h])

def getArea(x):
    l, w, h = x
    alls = a, b, c = l*w, w*h, l*h
    return 2*(a + b + c) + min(alls)

def getVolume(x):
    l, w, h = x
    return l*w*h

def getPerim(x):
    l, w, h = x
    alls = 2*(w+h), 2*(l+h), 2*(w+l)
    return min(alls) + getVolume(x)

totalArea = sum([getArea(present) for present in data])
totalPerimeter = sum([getPerim(present) for present in data])
print(f"Total area: {totalArea}")
print(f"Total perimeter: {totalPerimeter}")


