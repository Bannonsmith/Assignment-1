import unittest
from grocery import grocery_app


class GroceryAppTest(unittest.TestCase):
    def setUp(self):
        self.grocery = GroceryAppTest()
        print("SETUP")

    def test_multiply_two_numbers():
        print("test multiple two numbers")
        result = self.grocery.multiply (3,8)
