#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def max_integer(self):
        test = [1, 2, 32]
        result = max_integer(self)
        self.assertEqual(result, 32)

    def max_neg_int(self):
        test = [-4, -23, -1]
        result = max_neg_int(self)
        self.assertEqual(result, -1)

    def string_test(self):
        test = [1, 2, 'string']
        result = string_test(self)
        self.assertRaises(TypeError)

    def empty_list(self):
        test = []
        result = empty_list(self)
        self.assertEqual(result, None)

    def bool_list(self):
        test = [-2, -23, True]
        result = bool_list(self)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
