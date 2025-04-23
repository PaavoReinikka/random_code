# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:36:46 2022

@author: paavo
"""
import time

def maxdensity(dic): #density of subgraph
    a=0
    if(len(dic)==0):
        return a
    for i in dic.keys():
        a+=len(dic[i])
    #a=a/(2.0*len(dic)) # depending on your density definition
    a=a/len(dic)
    
    return a

def f_pop(dic,deg,counter): #
    tobedel=[]
    for i in deg.keys(): 
        if(deg[i]==counter):
            tobedel.append(i)
    for k in tobedel:
        for j in dic[k]:
            (dic[j]).remove(k)
            deg[j]=deg[j]-1
                 
        del dic[k]
        del deg[k]

def greedy_peel(dic,deg):
    
    start = time.time()
    D_G = maxdensity(dic)
    maxdens=0
    subgraph=[]
    while(len(deg)>0):
        print("Algo at work!")
        mindeg=float('inf')
        for i in deg.keys():
            mindeg= min(deg[i],mindeg)

        f_pop(dic,deg,mindeg)
        
        if (maxdensity(dic)>maxdens):
            maxdens=maxdensity(dic)
            print(dic)
            print(maxdens)
            subgraph=dic#.keys()
    
    #print(f"time: {time.time() - start}")
    print(subgraph)
    print(maxdens)
    print("D(G) = ",D_G)
    
    return subgraph