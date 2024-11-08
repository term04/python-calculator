import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(6, 3), 9)


    # Add the following test methods to the TestCalculator class:
    def test__subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(5, 5), 0)

    def test__multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(2, 2), 4)
        
    def test__divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(6, 2), 3)
        
    def test__modulo(self):
        self.assertEqual(self.calc.modulo(4, 2), 0)
        self.assertEqual(self.calc.modulo(11, 2), 1)

if __name__ == '__main__':
    unittest.main()