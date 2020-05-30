import numpy as np
from display import *
import cv2

cv2.namedWindow("sudoku",cv2.WINDOW_AUTOSIZE)

def isSafe(solvingGrid,r,c,x):
    for i in range(9):
        if solvingGrid[i][c]==x:
            return False

    for j in range(9):
        if solvingGrid[r][j]==x:
            return False

    rowSubGridStart = 3*(r//3)
    rowSubGridEnd = ((r//3)+1)*3-1
    columnSubGridStart = 3*(c//3)
    columnSubGridEnd = ((c//3)+1)*3-1

    rowLoop = rowSubGridStart
    columnLoop = columnSubGridStart

    while rowLoop<=rowSubGridEnd:
        while columnLoop<=columnSubGridEnd:
            if solvingGrid[rowLoop][columnLoop] == x:
                return False
            columnLoop += 1
        columnLoop = columnSubGridStart
        rowLoop += 1
    return True

def sudokuSolverUtil(grid,solvingGrid,r,c):
    if r==8 and c==8 and solvingGrid[r][c]!=0:
        return True
    if solvingGrid[r][c]!=0:
        if c==8:
            return sudokuSolverUtil(grid,solvingGrid,r+1,0)
        else:
            return sudokuSolverUtil(grid,solvingGrid,r,c+1)
    i = 1
    while i<=9:

        if isSafe(solvingGrid,r,c,i):

            solvingGrid[r][c] = i
            img = imageOfSudoku(grid, solvingGrid)
            cv2.imshow("sudoku", img)
            cv2.waitKey(100)
            if r == 8 and c == 8:
                return True


            if c == 8:
                temp = sudokuSolverUtil(grid,solvingGrid, r+1, 0)
            else:
                temp = sudokuSolverUtil(grid,solvingGrid, r, c+1)

            if temp:
                return True
            else:
                solvingGrid[r][c] = 0
                cv2.imshow("sudoku", img)
                cv2.waitKey(100)

        i += 1
    return False

def sudokuSolver(grid):
    solvedGrid = grid.copy()
    canBeSolved = sudokuSolverUtil(grid,solvedGrid,0,0)
    if canBeSolved:
        return solvedGrid
    else:
        return -1


grid = np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0],
                 [5, 2, 0, 0, 0, 0, 0, 0, 0],
                 [0, 8, 7, 0, 0, 0, 0, 3, 1],
                 [0, 0, 3, 0, 1, 0, 0, 8, 0],
                 [9, 0, 0, 8, 6, 3, 0, 0, 5],
                 [0, 5, 0, 0, 9, 0, 6, 0, 0],
                 [1, 3, 0, 0, 0, 0, 2, 5, 0],
                 [0, 0, 0, 0, 0, 0, 0, 7, 4],
                 [0, 0, 5, 2, 0, 6, 3, 0, 0]],np.int8)

x = sudokuSolver(grid)

img = imageOfSudoku(grid,x)
cv2.imshow("sudoku", img)
cv2.waitKey()
cv2.destroyAllWindows()
print(grid)
print(x)