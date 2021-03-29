# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:24:59 2021

@author: toona
Solver for SUdoku with backtracking recursive algorithm
"""

import numpy as np

backtracking = 0 #global variable

def get_avaible_cell(board):
        for i in range(0,9):
            for j in range(0,9):
                if(board[i,j] == 0):
                    return [i,j]
        return [-1,-1]
    
def get_block(i,j):
    p = i - i%3
    k = j - j%3
    return [p,k]

def validity_check(board,num,i,j):
    # check row
    if(num in board[i,:]):
        return False
    
    # check collumn
    if(num in board[:,j]):
        return False
    
    # check block
    [p,k] = get_block(i,j)
    block = board[p:p+3,k:k+3]
    if(num in block):
        return False   
    
    return True

def solve(board):
    
    [i,j]=get_avaible_cell(board)
    if([i,j] == [-1,-1]):
        return True
    
    for num in range(1,10,1):  
        # print(num)
        if(validity_check(board,num,i,j)):
            board[i,j] = num
            if(solve(board)):
                return True
            board[i,j] = 0    
        else:
            board[i,j] = 0 
    global backtracking
    backtracking +=1
    # print('backtracking')
    
    return False
            
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

input = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]

inp2  = [[5,1,7,6,0,0,0,3,4],
         [0,8,9,0,0,4,0,0,0],
         [3,0,6,2,0,5,0,9,0],
         [6,0,0,0,0,0,0,1,0],
         [0,3,0,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]

inpd  = [[1,0,5,7,0,2,6,3,8],
         [2,0,0,0,0,6,0,0,5],
         [0,6,3,8,4,0,2,1,0],
         [0,5,9,2,0,1,3,8,0],
         [0,0,2,0,5,8,0,0,9],
         [7,1,0,0,3,0,5,0,2],
         [0,0,4,5,6,0,7,2,0],
         [5,0,0,0,0,4,0,6,3],
         [3,2,6,1,0,7,0,0,4]]

hard  = [[8,5,0,0,0,2,4,0,0],
         [7,2,0,0,0,0,0,0,9],
         [0,0,4,0,0,0,0,0,0],
         [0,0,0,1,0,7,0,0,2],
         [3,0,5,0,0,0,9,0,0],
         [0,4,0,0,0,0,0,0,0],
         [0,0,0,0,8,0,0,7,0],
         [0,1,7,0,0,0,0,0,0],
         [0,0,0,0,3,6,0,4,0]]

diff  = [[0,0,5,3,0,0,0,0,0],
         [8,0,0,0,0,0,0,2,0],
         [0,7,0,0,1,0,5,0,0],
         [4,0,0,0,0,5,3,0,0],
         [0,1,0,0,7,0,0,0,6],
         [0,0,3,2,0,0,0,8,0],
         [0,6,0,5,0,0,0,0,9],
         [0,0,4,0,0,0,0,3,0],
         [0,0,0,0,0,9,7,0,0]]

board = np.array(grid)
solve(board)
print(board)
print('backtracking = ',backtracking)

board = np.array(input)
backtracking = 0
solve(board)
print(board)
print('backtracking = ',backtracking)

board = np.array(inp2)
backtracking = 0
solve(board)
print(board)
print('backtracking = ',backtracking)

board = np.array(inpd)
backtracking = 0
solve(board)
print(board)
print('backtracking = ',backtracking)

board = np.array(hard)
backtracking = 0
solve(board)
print(board)
print('backtracking = ',backtracking)

board = np.array(hard)
backtracking = 0
solve(board)
print(board)
print('backtracking = ',backtracking)