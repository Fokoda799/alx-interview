#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Return th weinner """
    def sieve(n):
        """Returns a list of primes up to n using the Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n ** 0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
        return [i for i, prime in enumerate(is_prime) if prime]

    # Variables to count wins
    maria_wins = 0
    ben_wins = 0

    for N in nums:
        primes = sieve(N)
        turn = 'Maria'

        # Game simulation: keep removing prime multiples until no more moves
        remaining_numbers = set(range(1, N + 1))
        while primes:
            # Find the smallest prime
            smallest_prime = primes.pop(0)
            # Remove all multiples of this prime
            multi = {i for i in remaining_numbers if i % smallest_prime == 0}
            if multi:
                remaining_numbers -= multi
            else:
                break

            # Switch turn
            if turn == 'Maria':
                turn = 'Ben'
            else:
                turn = 'Maria'

        # If Maria made the last valid move, she wins, otherwise Ben wins
        if turn == 'Ben':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None  # It's a tie
