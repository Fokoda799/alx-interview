#!/usr/bin/python3
""" Pascal triangle """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s
    triangle of n
    """
    if n <= 0:
        return []

    traingle = [[1]]

    for i in range(1, n):
        row = [1]
        pRow = traingle[i - 1]

        for j in range(1, len(pRow)):
            row.append(pRow[j - 1] + pRow[j])

        row.append(1)
        traingle.append(row)

    return traingle
