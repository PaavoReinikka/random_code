# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:05:06 2022

@author: paavo
"""
import numpy as np
import pandas as pd

def make_edge_and_degree_dict(filename):
    edges = []
    deg={}
    dic={}
    #start_time = time.clock() 
    file = open(filename,"r")  
    edges=file.readlines()
    for i in edges:
        #print("...")
        edge=list(map(int,i.split()))
        #print(edge)
        if edge[0] not in dic.keys():
            dic[edge[0]]=[]
            deg[edge[0]]=0
        dic[edge[0]].append(edge[1])
        deg[edge[0]]+=1
    
        if edge[1] not in dic.keys():
            dic[edge[1]]=[]
            deg[edge[1]]=0
        dic[edge[1]].append(edge[0])
        deg[edge[1]]+=1
            
    file.close()
    return dic, deg

def make_adjacency_matrix(dic):
    #dic, _ = make_edge_and_degree_dict(filename)
    nodes = len(list(dic.keys()))
    M = np.zeros((nodes, nodes))
    keys, values = list(dic.keys()), list(dic.values())
    for i in range(len(keys)):
        M[keys[i]-1,np.asarray(values[i])-1]=1
    return M

    