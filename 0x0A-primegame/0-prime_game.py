#!/usr/bin/python3
""" A function to determine the winner of a game """


def is_prime(num):
    """ A function to check if a number is prime """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ A function to determine the winner of a game """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of prime numbers in the range
        primes_count = sum(1 for i in range(2, n+1) if is_prime(i))

        # If number of primes is even, Ben wins
        # If number of primes is odd, Maria wins
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
