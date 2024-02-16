#!/usr/bin/python3
"""You have n number of locked boxes in front of you. 
Each box is numbered sequentially from 0 to 
n - 1 and each box may contain keys to the other boxes
"""

def pascal_triangle(n):
    """A function that returns a list of lists 
    of integers representing the Pascal’s triangle of n:
    """

    triangle = [[1], [1, 1]]

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    for i in range(2, n):
        triangle.append([1])
        it = triangle[i - 1]

        for j in range(1, len(it)):
            triangle[i].append(it[j] + it[j - 1])
        triangle[i].append(1)

    return triangle