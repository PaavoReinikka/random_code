# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 19:00:22 2024

@author: paavo
"""

import numpy as np

class Map(object):
    def __init__(self,  M):
        self.pos = np.where(M=="^")
        self.dir="^"
        self.map=M
        self.xmax=M.shape[1]
        self.ymax=M.shape[0]
        
    def turn(self):
        match self.dir:
            case "^":
                self.dir=">"
            case ">":
                self.dir="v"
            case "v":
                self.dir="<"
            case "<":
                self.dir="^"
            case default:
                print("Direction error")

    def move(self):
        match self.dir:
            case "^":
                self.pos = (np.array(self.pos[0]-1),np.array(self.pos[1]))
            case ">":
                self.pos = (np.array(self.pos[0]),np.array(self.pos[1]+1))
            case "v":
                self.pos = (np.array(self.pos[0]+1),np.array(self.pos[1]))
            case "<":
                self.pos = (np.array(self.pos[0]),np.array(self.pos[1]-1))
            case default:
                print("Move error")
                
    def peek(self):
        match self.dir:
            case "^":
                return self.peekup()
            case ">":
                return self.peekright()
            case "v":
                return self.peekdown()
            case "<":
                return self.peekleft()
            case default:
                print("Peek error")
                return None
            
    def color(self):
        if self.map[self.pos]==".":
            self.map[self.pos]="X"
        
        
    def peekup(self):
        if self.pos[0]==0:
            self.color()
            print("EXIT")
            return "EXIT"
        return M[self.pos[0]-1,self.pos[1]]
    
    def peekright(self):
        if self.pos[1]==self.xmax-1:
            self.color()
            print("EXIT")
            return "EXIT"
        return M[self.pos[0],self.pos[1]+1]
    
    def peekdown(self):
        if self.pos[0]==self.ymax-1:
            self.color()
            print("EXIT")
            return "EXIT"
        return M[self.pos[0]+1,self.pos[1]]
    
    def peekleft(self):
        if self.pos[1]==0:
            self.color()
            print("EXIT")
            return "EXIT"
        return M[self.pos[0],self.pos[1]-1]
            

M=[]
with open("input.txt") as f:
    lines=f.readlines()
    for line in lines:
        tmp = [char for char in line.strip()]
        M.append(tmp)
        
M=np.array(M)

count=0
game=Map(M)
while True:
    peek=game.peek()
    if peek=="#":
        game.turn()
    elif peek=="EXIT":
        break
    else:
        game.color()
        game.move()
        count+=1
    
print(np.sum(game.map=="X"))













    
    