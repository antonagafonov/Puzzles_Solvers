# https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1
# from Geeks
class Solution:
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=" ")
        print()
    
    def used_in_row(self,arr,row,num):
        for i in range(9):
            if(arr[row][i] == num):
                return True
        return False
    
    def used_in_col(self,arr,col,num):
        for i in range(9):
            if(arr[i][col] == num):
                return True
        return False
    
    def used_in_box(self,arr,row,col,num):
        for i in range(3):
            for j in range(3):
                if(arr[i+row][j+col] == num):
                    return True
        return False
    
    def check_location_is_safe(self,arr,row,col,num):
        return not self.used_in_row(arr,row,num) and not self.used_in_col(arr,col,num) and not self.used_in_box(arr,row - row%3,col - col%3,num)
    
    def find_empty_location(self,arr,l):
        for row in range(9):
            for col in range(9):
                if(arr[row][col]==0):
                    l[0]=row
                    l[1]=col
                    return True
        return False
    
    def SolveSudoku(self,grid):
        l=[0,0]
    
        if(not self.find_empty_location(grid,l)):
            return True
    
        row=l[0]
        col=l[1]
    
        for num in range(1,10):
    
            if(self.check_location_is_safe(grid,row,col,num)):
    
                grid[row][col]=num
    
                if(self.SolveSudoku(grid)):
                    return True
    
                grid[row][col] = 0
    
        return False

