# -*- coding: utf-8 -*-
"""
Created/updated on 29 Dec 2025
-- changed to use defaultdict for efficiency/brevity
@author: paavo
"""
import numpy as np
from collections import defaultdict

def make_edge_and_degree_dict(filename):
    edges = []
    deg=defaultdict(int)
    dic=defaultdict(list)
    file = open(filename,"r")  
    edges=file.readlines()
    for i in edges:
        edge=list(map(int,i.split()))
 
        dic[edge[0]].append(edge[1])
        deg[edge[0]]+=1

        # imposing undirectedness
        dic[edge[1]].append(edge[0])
        deg[edge[1]]+=1
            
    file.close()
    return dic, deg

def make_adjacency_matrix(dic):
    nodes = len(list(dic.keys()))
    M = np.zeros((nodes, nodes))
    keys, values = list(dic.keys()), list(dic.values())
    for i in range(len(keys)):
        M[keys[i]-1,np.asarray(values[i])-1]=1
    return M

    