import unittest
import calc


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(5, 5), 10)
        self.assertEqual(calc.add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 10), 0)
        self.assertEqual(calc.subtract(10, 100), -90)
        self.assertEqual(calc.subtract(-10, -10), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 10), 100)
        self.assertEqual(calc.multiply(7, 4), 28)
        self.assertEqual(calc.multiply(3, -9), -27)

    def test_divide(self):
        self.assertEqual(calc.divide(49, 7), 7)
        self.assertEqual(calc.divide(50, 5), 10)
        self.assertEqual(calc.divide(98, 7), 14)




if __name__ == '__main__':
    unittest.main()