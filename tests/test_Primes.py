"""
Unit tests for Primes package
"""
import unittest
from desc.primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """
    TestCase class for is_prime function.
    """
    def test_two_is_prime(self):
        "Test that two is prime."
        self.assertTrue(is_prime(2))

    def test_three_is_prime(self):
        "Test that three is prime."
        self.assertTrue(is_prime(3))

    def test_four_is_not_prime(self):
        "Test that four is not prime."
        self.assertFalse(is_prime(4))

    def test_five_is_prime(self):
        "Test that five is prime."
        self.assertTrue(is_prime(5))


if __name__ == '__main__':
    unittest.main()
