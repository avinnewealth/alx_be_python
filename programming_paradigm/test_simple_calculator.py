import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculators(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 1), 3)
        self.assertEqual(self.calc.add(-2,3),1)
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(-2,3),-5)
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)
        self.assertEqual(self.calc.multiply(-2,3),-6)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(-6,3),-2)
        self.assertEqual(self.calc.divide(0, 5), 0)

        self.assertIsNone(self.calc.divide(5, 0))