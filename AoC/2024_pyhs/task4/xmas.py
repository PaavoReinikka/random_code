# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 23:11:24 2024

@author: paavo
"""

import numpy as np


def right(i,j):
    b=False
    if(j+3<n):
        if(M[i,j]=="X"):
            b = M[i,j+1]=="M"
            b &= M[i,j+2]=="A"
            b &= M[i,j+3]=="S"
        elif M[i,j]=="S":
            b = M[i,j+1]=="A"
            b &= M[i,j+2]=="M"
            b &= M[i,j+3]=="X"
#    if(j+3<n):
#        b = (M[i,j:j+4]=="XMAS").all()
#        b|= (M[i,j:j+4]=="SAMX").all()
#        return b
#    return False
    return b


def rightDown(i,j):
    b=False
    if(j+3<n and i+3<n):
        if M[i,j]=="X":
            b = M[i+1,j+1]=="M"
            b &= M[i+2,j+2]=="A"
            b &= M[i+3,j+3]=="S"
        elif M[i,j]=="S":
            b = M[i+1,j+1]=="A"
            b &= M[i+2,j+2]=="M"
            b &= M[i+3,j+3]=="X"
    return b

def down(i,j):
    b=False
    if(i+3<n):
        if M[i,j]=="X":
            b = M[i+1,j]=="M"
            b &= M[i+2,j]=="A"
            b &= M[i+3,j]=="S"
        elif M[i,j]=="S":
            b = M[i+1,j]=="A"
            b &= M[i+2,j]=="M"
            b &= M[i+3,j]=="X"
    return b 

    
def leftDown(i,j):
    b=False
    if(i+3<n and 0<=j-3):
        if M[i,j]=="X":
            b = M[i+1,j-1]=="M"
            b &= M[i+2,j-2]=="A"
            b &= M[i+3,j-3]=="S"
        elif M[i,j]=="S":
            b = M[i+1,j-1]=="A"
            b &= M[i+2,j-2]=="M"
            b &= M[i+3,j-3]=="X"
    return b            
    


i=0
with open("input.txt") as f:
    lines = f.readlines()
    n=len(lines[0].strip())
    for line in lines:
        assert len(line.strip())==n
        i+=1
        
M = np.empty((i,n), dtype=str)
for i,line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        M[i,j]=char

acc=0
for i in range(n):
    for j in range(n):
        acc+=right(i, j)
        acc+=rightDown(i, j)
        acc+=down(i, j)
        acc+=leftDown(i, j)



def check(i,j):
    if M[i,j]=="A":
        left = M[i-1,j-1] + "A"
        left+= M[i+1,j+1]
        right = M[i+1,j-1] + "A"
        right+= M[i-1,j+1]
        
        bleft = left=="MAS" or left=="SAM"
        bright = right=="MAS" or right=="SAM"
        return bright and bleft
    return False

acc2=0
for i in range(1,n-1):
    for j in range(1,n-1):
        acc2+=check(i,j)
        











        