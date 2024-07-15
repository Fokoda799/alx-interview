#!/usr/bin/python3
""" Pascal traingle """


def pascal_traingle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows of Pascal's Triangle to generate.

    Returns:
        list of list of int: A list of lists representing Pascal's Triangle.

    Examples:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
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

