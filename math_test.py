"""Sw metrics exam"""
import unittest
import math

class CalculatorTest(unittest.TestCase):
    "Math test"
    def test_add(self):
        "Test if addition is working"
        self.assertEqual(10, 3+7)

    def test_subtract(self):
        "Test if subtraction is working"
        self.assertEqual(12,15 - 3)

    def test_factoriel(self):
        "Test if factoriel is working"
        self.assertEqual(6, math.factorial(3) )

    def test_multiply(self):
        "Test if multiplication is working"
        self.assertEqual(30, 5 * 6)
