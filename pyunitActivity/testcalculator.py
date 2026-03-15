import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(3, 2),5)
        self.assertNotEqual(Calculator.add(3, 2), 6)
        self.assertTrue(Calculator.add(3, 2))

    def test_subtract(self):
        self.assertFalse(Calculator.subtract(3, 3))
        self.assertNotEqual(Calculator.subtract(3, 3), 8)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 2),6)
        self.assertNotEqual(Calculator.multiply(3, 2), 90)
    
    def test_divide(self):
        self.assertEqual(Calculator.divide(3, 2),1.5)
        self.assertNotEqual(Calculator.divide(3, 2), 2)

if __name__ == "__main__":
    unittest.main()