#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(limit):
    """Generates a list of primes up to the limit
    using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] is True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]


def count_primes_up_to(n, primes):
    """Counts the number of primes up to n."""
    count = 0
    for prime in primes:
        if prime > n:
            break
        count += 1
    return count


def isWinner(x, nums):
    """ Return the Winner """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    players = {'Maria': 0, 'Ben': 0}

    for num in nums:
        prime_count = count_primes_up_to(num, primes)

        # Determine the winner based on the count of primes
        if prime_count % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None
