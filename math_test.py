import unittest

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(10, 3+7)

