# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 17:45:15 2022

@author: paavo
"""
import numpy as np
import matplotlib.pyplot as plt

data= \
[('A',105), ('B', 110), ('A', 120), ('C',122), ('A',130), ('B',135),
('C',185), ('A', 195), ('C', 220), ('A',260), ('B',270), ('C',295),
('A',420), ('C', 440), ('B', 445), ('C',522), ('A',530), ('B',555)]

data2 = \
[('A',104), ('B', 109), ('A', 119), ('C',121), ('A',129), ('B',134),
('C',184), ('A', 194), ('C', 219), ('A',259), ('B',269), ('C',294),
('A',419), ('C', 439), ('B', 444), ('C',521), ('A',529), ('B',554)]

data3 = \
[('A',0), ('B', 5), ('A', 15), ('C',17), ('A',25), ('B',30),
('C',80), ('A', 90), ('C', 115), ('A',155), ('B',165), ('C',190),
('A',315), ('C', 335), ('B', 340), ('C',417), ('A',425), ('B',450)]    


As=[105,120,130,195,260,420,530]
#  [  0,  15,  25,  90, 155, 315, 425]
Bs=[110,135,270,445,555]
#  [  5,  30, 165, 340, 450]
Cs=[122,185,220,295,440,522]
#  [ 17,  80, 115, 190, 335, 417]
n_A=7
n_B=5
n_C=6

def make_data_dict(data):
    l = []
    for elem in data:
        l.append((elem[1],elem[0]))
    return dict(l)


def make_data_arr(dic):
    mapping = {'A':1,'B':2,'C':3}
    n = max(dic.keys()) + 1
    arr = np.zeros((n,))
    for i in range(n):
        if(i in dic.keys()):
            arr[i]=mapping[dic[i]]
    return arr

def make_all(data):
    dic = make_data_dict(data)
    arr = make_data_arr(dic)
    ind = list(dic.keys())

    return arr, ind


def f_arr(S,anticedent,consequent,w,verbose=False):
    n=len(S)
    accum=0
    base=0
    
    for head in range(n-1):
        if(S[head]==anticedent):
            base+=1
            for tail in range(head,head + w):
                if(tail>=n):
                    break
                if(S[tail]==consequent):
                    accum+=1
                    break
    
    result = accum / base
    if(verbose):
        print('%d anticedents' % base)
        print('%d events matching conditions' % accum)
        print('f = %f' % result)
    return result

def randomization(data,n_iter,w):
    arr,ind = make_all(data)
    fs = np.zeros((n_iter,))
    vals = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
    
    for i in range(n_iter):
        z=np.zeros_like(arr)
        new_ind = np.random.choice(ind,len(ind),replace=False)
        for j in range(len(new_ind)):
            z[new_ind[j]]=vals[j]
        fs[i]=f_arr(z,1,2,w,False)
        #print(fs[i])
        
    f_base = f_arr(arr,1,2,w,False)
    plt.hist(fs)
    plt.vlines(f_base,ymin=0,ymax=n_iter/10,color='red')
    plt.title("{} iter p_emp ~ {}".format(n_iter,np.mean(fs>f_base)))
    plt.show()
    return f_base,fs,np.mean(fs>f_base)
    
def randomization_naive(data,n_iter,w):
    arr,ind = make_all(data)
    fs = np.zeros((n_iter,))
    vals = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
    
    for i in range(n_iter):
        z=np.zeros_like(arr)
        new_ind = np.random.choice(range(len(arr)),len(ind),replace=False)
        for j in range(len(new_ind)):
            z[new_ind[j]]=vals[j]
        fs[i]=f_arr(z,1,2,w,False)
        #print(fs[i])
        
    f_base = f_arr(arr,1,2,w,False)
    plt.hist(fs)
    plt.vlines(f_base,ymin=0,ymax=n_iter/10,color='red')
    plt.title("{} iter p_emp ~ {}".format(n_iter,np.mean(fs>f_base)))
    plt.show()
    return f_base,fs,np.mean(fs>f_base)
    

def f(S,anticedent, consequent, w, verbose=False):
    n=len(S)
    accum=0
    base=0
    
    for head in range(n-1):
        if(S[head][0]==anticedent):
            base+=1
            for tail in range(head,n):
                if(S[tail][1] - S[head][1] > w):
                    break
                if(S[tail][0]==consequent):
                    print(S[head])
                    print(S[tail])
                    print('------')
                    accum+=1
                    break
    
    result = accum / base
    print('%d anticedents' % base)
    print('%d events matching conditions' % accum)
    print('f = %f' % result)
    return result
    