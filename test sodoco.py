import numpy as np
from math import *

class sudoku():
    def __init__(self):
        self.board  = np.zeros((9,9), dtype=int) # start with blank board
        #self.__fill_cell(0)
        
    def fill_cell(self,k):
        if k==81:
            return True
            
        i = k // 9
        j = k % 9
        if self.board[i,j]!=0:
            if self.fill_cell(k+1):
                return True
            
            k=k-1
            return False
        
        elif self.board[i,j]==0:
            row = set(self.board[i,:])
            column = set(self.board[:,j])
            square = set(self.board[(i//3)*3:(1+i//3)*3,(j//3)*3:(1+j//3)*3].flatten())
            usedNumSet = row.union(column).union(square)
            # pick a number for cell (i,j) from the set of remaining available numbers        
            choices = list(set(range(1,10)).difference(usedNumSet))
            np.random.shuffle(choices)
            for choice in choices:
                self.board[i,j] = choice
                if self.fill_cell(k+1):
                    return True
            self.board[i,j] = 0
            return False
        
            
            
            
    def get_puzzle(self, n=45):
        mask = np.array([0]*n+[1]*(81-n),dtype=int)
        np.random.shuffle(mask)
        return mask.reshape(9,9) * self.board

    def get_solution(self):
        return self.board

b=[[0,0,0,0,7,0,0,0,0],
   [0,0,0,1,0,0,0,0,0],
   [0,0,0,0,0,0,0,6,0],
   [8,0,0,0,6,0,0,0,3],
   [4,0,0,0,0,3,0,0,1],
   [7,0,0,0,2,0,0,0,6],
   [0,6,0,0,0,0,2,8,0],
   [0,0,0,4,0,9,0,0,5],
   [0,0,0,0,0,0,0,0,9]]
mysudoku = sudoku()
n=0
for i in range (0,9):
    for j in range (0,9):
        if b[i][j]!=0:
            mysudoku.board[i][j]=b[i][j]
            n+=1
f=[]
repeat=0
counter=1
while repeat<=sqrt(n):
    #print (mysudoku.board)
    mysudoku.fill_cell(0)
    if f.count(mysudoku.get_solution())!=0:
        repeat+=1
    if f.count(mysudoku.get_solution())==0:

        #print(mysudoku.get_puzzle()
        f.append(mysudoku.get_solution())
        #print (f)
        print("solution ",counter)
        print(mysudoku.get_solution())
        counter+=1



