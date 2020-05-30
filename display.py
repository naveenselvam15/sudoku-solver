import cv2
import numpy as np

def imageOfSudoku(grid,solvingGrid):
    """
    this function returns the image of the sudoku with
    grid of already given numbers in white color and
    other computing numbers in green color.

    parameters :

    grid - grid of given numbers
    solvingGrid - grid of numbers came up while backtracking algo runs

    """

    img = np.ones((450, 450, 3), np.uint8)
    cv2.line(img, (0, 150), (450, 150), (255, 255, 255), 3)
    cv2.line(img, (0, 300), (450, 300), (255, 255, 255), 3)
    cv2.line(img, (150, 0), (150, 450), (255, 255, 255), 3)
    cv2.line(img, (300, 0), (300, 450), (255, 255, 255), 3)

    i = 1
    j = 1

    while i <= 8:
        cv2.line(img, (i * 50, 0), (i * 50, 450), (255, 255, 255), 1)
        i += 1
    while j <= 8:
        cv2.line(img, (0, j * 50), (450, j * 50), (255, 255, 255), 1)
        j += 1


    for i in range(9):
        for j in range(9):
            if grid[i][j]!=0:
                cv2.putText(img, str(grid[i][j]), (j*50+15, i*50+35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            elif solvingGrid[i][j]!=0:
                cv2.putText(img, str(solvingGrid[i][j]), (j* 50+15, i*50+35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return img