#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """ Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0

    db = [0] + [float('inf')] * total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                db[i] = min(db[i], db[i - coin] + 1)

    return db[total] if db[total] != float('inf') else -1
