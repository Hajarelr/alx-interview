#!/usr/bin/python3
"""Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
       Rotates 2D matrix 90 degrees clockwise
       Matrix is edited in-place
       args:
          matrix
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for n in range(right - left):
            top, bottom = left, right
            # save topleft  value
            topLeft = matrix[top][left + n]
            # move bottom left to top left
            matrix[top][left + n] = matrix[bottom - n][left]
            # move bottom right to bottom left
            matrix[bottom - n][left] = matrix[bottom][right - n]
            # move top right to bottom right
            matrix[bottom][right - n] = matrix[top + n][right]
            # move top left to top right
            matrix[top + n][right] = topLeft
        right -= 1
        left += 1
