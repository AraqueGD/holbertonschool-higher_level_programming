#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def TestNone(self):
        """ Send None in Function """
        self.assertIsNone(max_integer([]))

    def TestRaises(self):
        """
            Send Parameter None in Function
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def Test_begining(self):
        """
            Send First great Number
        """
        self.assertEqual(max_integer([100, 1, 1, 1]), 100)
