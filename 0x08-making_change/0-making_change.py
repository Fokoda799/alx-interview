#!/usr/bin/python3
"""
Main file for testing
"""

from collections import deque


def makeChange(coins, total):
    """ Return the minimum number of coins needed to make up the total. """
    if total <= 0:
        return 0

    queue = deque([(0, 0)])
    visited = set()

    while queue:
        current, num_coins = queue.popleft()

        for coin in coins:
            next_amount = current + coin

            if next_amount == total:
                return num_coins + 1
            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, num_coins + 1))

    return -1
