#!/usr/bin/python3
"""Module to find the max integer in a list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_docstring(self):
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_func_doc(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_emptyargs(self):
        self.assertIsNone(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 2, None])

    def test_integers(self):
        self.assertEqual(max_integer([1, 7, 8]), 8)

    def test_neginteger(self):
        self.assertEqual(max_integer([-1, -2, -30]), -1)

    def test_alpha(self):
        self.assertEqual(max_integer(["xyz"]), "xyz")

if __name__ == "__main__":
    unittest.main()