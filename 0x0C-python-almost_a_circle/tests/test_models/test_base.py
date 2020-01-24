#!/usr/bin/python3
""" Unit Testing for Models/base.py """

import unittest
from models.base import Base


class Test_Base_Class_id(unittest.TestCase):
    """ Tests Class Base Id """

    def test_id(self):
        """ Test id receives void as input parameter """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_None(self):
        """ Test id receives None as input parameter """
        b3 = Base(None)
        self.assertEqual(b3.id, 3)

    def test_id_parameter(self):
        """ Test id receives Number as input parameter """
        b4 = Base(8)
        self.assertEqual(b4.id, 8)

    def test_id_public(self):
        """ Test id Change in instance after receives Base parameter """
        b5 = Base(18)
        b5.id = 15
        self.assertEqual(b5.id, 15)

    def test_id_string(self):
        """ Test id eceives String as input parameter """
        b6 = Base("test")
        self.assertEqual(b6.id, "test")


if __name__ == "__main__":
    unittest.main()
