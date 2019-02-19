import unittest
from Calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        print("setUp")

    def test_add_two_numbers(self):
        print("test add two numbers")
        result = self.calculator.add(3,5)
        self.assertEqual(5,result)
