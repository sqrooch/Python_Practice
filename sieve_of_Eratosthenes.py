"""
In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
This module contains an algorithm that finds all prime numbers up to a given limit and returns their number.
"""


def sieve_of_eratosthenes(n):
    """Finds all prime numbers up to the given limit and returns their number.
    An array of prime numbers will also be printed to the console screen.
    The argument n is a natural integer that is the upper limit of the number range under consideration."""

    primes_highlighter = [True] * (n+1)
    primes_highlighter[0] = primes_highlighter[1] = False
    primes_counter = 0

    for i in range(2, n+1):
        if primes_highlighter[i]:
            primes_counter += 1
            for j in range(2*i, n+1, i):
                primes_highlighter[j] = False

    print("\nYou have the following array of primes in your chosen range: ")
    for i in range(n+1):
        if primes_highlighter[i]:
            print(i, end=" ")

    return primes_counter


userInput = int(input("\nEnter here the upper limit of the range to find the number of all primes in it: "))
print(f"\nThere are {sieve_of_eratosthenes(userInput)} primes in the range you suggested.")
