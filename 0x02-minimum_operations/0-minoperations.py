#!/usr/bin/python3
""" Min oprations """


def minOperations(n):
    """
    Calculates the minimum operations to reach n H characters.

    Args:
        n: The target number of H characters.

    Returns:
        The minimum number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0

    op = 0
    factor = 2
    while n > 1:
        if n % factor == 0:
            n //= factor
            op += factor
        else:
            factor += 1

    return op
