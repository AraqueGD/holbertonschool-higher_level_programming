#!/usr/bin/python3
""" Unit Testing for Models/base.py """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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


class test_to_json_string(unittest.TestCase):
    """ Testing Convert String Dict to Json in Class Base"""

    def test_to_json_string(self):
        r_test = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(
            str, type(Base.to_json_string([r_test.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r_test = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string(
            [r_test.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r_test = Rectangle(2, 3, 5, 19, 2)
        r_test2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r_test.to_dictionary(), r_test2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s_test = Square(10, 2, 3, 4)
        self.assertEqual(
            str, type(Base.to_json_string([s_test.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual([], Base.to_json_string(None))

    def test_to_json_string_notargs(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 2)


if __name__ == "__main__":
    unittest.main()
