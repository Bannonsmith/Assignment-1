import unittest
from mycode import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        print("test_hello")
        self.assertEqual(hello_world(), 'Hello World')

        def test_custom_num_list(self):
            self.assertEqual(len(create_num_list(10)), 10)

unittest.main()
