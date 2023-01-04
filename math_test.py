import unittest
import math

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(10, 3+7)

    def test_subtract(self):
        self.assertEqual(12,15 - 3)

    def test_factoriel(self):
        self.assertEqual(6, math.factorial(3) )

    def test_multiply(self):
        self.assertEqual(30, 5 * 6)
