#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Return the winner """
    if x == 0 or not nums:
        return None

    max_num = max(nums)

    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        # Check the number of primes that can be removed up to n
        primes_removed = prime_count[n]

        # If the number of primes removed is odd, Maria wins (she goes first)
        # If even, Ben wins
        if primes_removed % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 3: Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
