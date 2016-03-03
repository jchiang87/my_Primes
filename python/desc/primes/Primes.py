"""
Module to test for primes.
"""


def is_prime(number):
    "Test if number is prime."

    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True
