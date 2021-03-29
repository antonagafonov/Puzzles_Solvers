# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:50:04 2021

@author: toona
Solver for N Queens Puzzle
"""

import numpy as np

backtracking = 0 #global variable

def sum_of_diagonals(row,collumn,board,N):
    # this function sums 2 diagonals from defined [i,j] cell and returns max 
    # of those two diagonals
    diagonal_sum_1=0
    diagonal_sum_2=0
    # check the first diagonal
    for i in range(0,N,1):
        if ((row + i == N) or (collumn + i == N)):
            break
        diagonal_sum_1 += board[row + i,collumn + i]
    for i in range(1,N,1):
        if ((row - i == -1) or (collumn - i == -1)):
            break
        diagonal_sum_1 += board[row - i,collumn - i]
    # check the second diagonal    
    for i in range(0,N,1):
        if ((row + i == N) or (collumn - i == -1)):
            break
        diagonal_sum_2 += board[row + i,collumn - i]
    for i in range(1,N,1):
        if ((row - i == -1) or (collumn + i == N)):
            break
        diagonal_sum_2 += board[row - i,collumn + i] 
        
    return max(diagonal_sum_1,diagonal_sum_2)
                

def valid_location(row,collumn,board,N):
    # this function checks if location for defined [i,j] cell is valid 
    # first check row sum,if it > 1 returns False ,location invalid
    # secod checks sum of diagonals ,if > 1 returns False,location invalid
    collumn_sum = np.sum(board,axis=1)

    if (collumn_sum[row] > 1):
        return False
    if (sum_of_diagonals(row,collumn,board,N) > 1):       
        return False
    
    return True
        
        
def solve(N,board,collumn):
    # solves for given board and collumn location
    # return True if solved the board
    # return False if conditions is not valid
    if (collumn==N):
        return True #Puzzel solved
    
    for row in range(0,N):   
            # Try to place Queen in current location
            board[row,collumn] = 1
            # checks if location is valid
            if(valid_location(row,collumn,board,N)):  
                # if location is valid go to next collumn 
                # and try to solve from there
                if (solve(N,board,collumn + 1)):
                    return True
                # if tryed all rows and not satisfied game rules
                # make current cell 0 and try to assign the next row
                board[row,collumn] = 0
            else:
                # if current cell is not valid assign 0 to it 
                # and go to next iteration to try following row
                board[row,collumn] = 0
    # count nuber of backtrackings for the run
    global backtracking 
    backtracking += 1
    # print('backtracking')
    return False
                
N = 18
board = np.zeros((N,N))

solve(N,board,collumn = 0)
print('backtracking = ',backtracking)
print(board)
