import numpy as np
from display import *
import cv2


def isSafe(solvingGrid, r, c, x):

    """
    This function checks whether a number (0-9) is
    safe to be occupied in specified cell of sudoku

    :param solvingGrid: grid of numbers computed by backtracking algo
    :param r: row index
    :param c: column index
    :param x: number to be checked
    :return: boolean value

    """
    for i in range(9):
        if solvingGrid[i][c] == x:
            return False

    for j in range(9):
        if solvingGrid[r][j] == x:
            return False

    rowSubGridStart = 3*(r//3)
    rowSubGridEnd = ((r//3)+1)*3-1
    columnSubGridStart = 3*(c//3)
    columnSubGridEnd = ((c//3)+1)*3-1

    rowLoop = rowSubGridStart
    columnLoop = columnSubGridStart

    while rowLoop <= rowSubGridEnd:
        while columnLoop <= columnSubGridEnd:
            if solvingGrid[rowLoop][columnLoop] == x:
                return False
            columnLoop += 1
        columnLoop = columnSubGridStart
        rowLoop += 1
    return True

def sudokuSolverUtil(grid, solvingGrid, r, c):

    """
    This function solves sudoku by backtracking algorithm
    and displays the algorithm computation
    :param grid: grid of given numbers
    :param solvingGrid: grid of numbers came up while backtracking algo runs
    :param r: row index
    :param c: column index
    :return: boolean value
    returns true if game can be solved or else returns false
    """

    if r == 8 and c == 8 and solvingGrid[r][c] != 0:
        return True
    if solvingGrid[r][c] != 0:
        if c == 8:
            return sudokuSolverUtil(grid, solvingGrid, r+1, 0)
        else:
            return sudokuSolverUtil(grid, solvingGrid, r, c+1)
    i = 1
    while i <= 9:

        if isSafe(solvingGrid, r, c, i):

            solvingGrid[r][c] = i
            img = imageOfSudoku(grid, solvingGrid)
            cv2.imshow("SUDOKU", img)
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
                cv2.imshow("SUDOKU", img)
                cv2.waitKey(100)

        i += 1
    return False

def sudokuSolver(grid):

    """
    This function solves the sudoku game.
    :param grid: grid of numbers with some empty cells. (occupied by zeros)
    :return: solved sudoku when it is possible to solve or else
    returns -1.
    """

    solvedGrid = grid.copy()
    canBeSolved = sudokuSolverUtil(grid, solvedGrid, 0, 0)
    if canBeSolved:
        return solvedGrid
    else:
        return -1

if __name__ == '__main__':

    cv2.namedWindow("SUDOKU", cv2.WINDOW_AUTOSIZE)

    grid = np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0],
                     [5, 2, 0, 0, 0, 0, 0, 0, 0],
                     [0, 8, 7, 0, 0, 0, 0, 3, 1],
                     [0, 0, 3, 0, 1, 0, 0, 8, 0],
                     [9, 0, 0, 8, 6, 3, 0, 0, 5],
                     [0, 5, 0, 0, 9, 0, 6, 0, 0],
                     [1, 3, 0, 0, 0, 0, 2, 5, 0],
                     [0, 0, 0, 0, 0, 0, 0, 7, 4],
                     [0, 0, 5, 2, 0, 6, 3, 0, 0]],np.int8)

    solvedGrid = sudokuSolver(grid)

    img = imageOfSudoku(grid, solvedGrid)
    cv2.imshow("SUDOKU", img)
    print(solvedGrid)

    cv2.waitKey()
    cv2.destroyAllWindows()
