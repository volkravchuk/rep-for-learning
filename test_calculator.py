import unittest
import utilities.calculator as calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.Calculator.add(10, 5), 15)
        self.assertEqual(calculator.Calculator.add(-1, 1), 0)
        self.assertEqual(calculator.Calculator.add(1, -1), 0)
        self.assertEqual(calculator.Calculator.add(-2, -2), -4)

    def test_substract(self):
        self.assertEqual(calculator.Calculator.substract(10, 5), 15)
        self.assertEqual(calculator.Calculator.substract(-1, 1), 0)
        self.assertEqual(calculator.Calculator.substract(1, -1), 0)
        self.assertEqual(calculator.Calculator.substract(-2, -2), -4)

    def test_multiply(self):
        self.assertEqual(calculator.Calculator.multiply(10, 5), 15)
        self.assertEqual(calculator.Calculator.multiply(-1, 1), 0)
        self.assertEqual(calculator.Calculator.multiply(1, -1), 0)
        self.assertEqual(calculator.Calculator.multiply(-2, -2), -4)
        
    def test_divide(self):
        self.assertEqual(calculator.Calculator.divide(10, 5), 15)
        self.assertEqual(calculator.Calculator.divide(-1, 1), 0)
        self.assertEqual(calculator.Calculator.divide(1, -1), 0)
        self.assertEqual(calculator.Calculator.divide(-2, -2), -4)


if __name__ == '__main__':
    unittest.main()