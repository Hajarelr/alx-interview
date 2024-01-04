#!/usr/bin/python3
"""Script to determine pascal's triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for m in range(n):
        temp_list = []

        for i in range(m+1):
            if i == 0 or i == m:
                temp_list.append(1)
            else:
                temp_list.append(triangle[m-1][i-1] + triangle[m-1][i])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
