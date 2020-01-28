#!/usr/bin/python3
""" Unit Testing for Models/square.py """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square_class(unittest.TestCase):
    """ Testing Square Class """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_one_arg(self):
        """ Test in Square receives one arg """
        with self.assertRaises(TypeError):
            Square()

    def test_two_arg(self):
        """ Test in Square receives two arg """
        s_test = Square(12, 2)
        self.assertEqual(s_test.id, 1)

    def test_three_arg(self):
        """ Test in Square receives three arg """
        s_test = Square(23, 4, 2)
        self.assertEqual(s_test.id, 1)

    def test_four_arg(self):
        """ Test in Square receives four arg """
        s_test = Square(13, 4, 9, 5)
        self.assertEqual(s_test.id, 5)

    def test_limited_arg(self):
        """ Test for limited arguments """
        with self.assertRaises(TypeError):
            s_test = Square(13, 4, 9, 5, 10)

    def test_None_arg(self):
        """ Test in Square receives None arg """
        with self.assertRaises(TypeError):
            Square(None)

    def test_Private_size(self):
        """ Test in Square Acces for Private Attribute """
        with self.assertRaises(AttributeError):
            print(Square(2, 4, 5, 6).__width)

    def test_Private_height(self):
        """ Test in Square Acces for Private Attribute """
        with self.assertRaises(AttributeError):
            print(Square(2, 4, 5, 6).__height)


class test_Raises_Validation(unittest.TestCase):
    """ Test size, height, x and y Validation """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_size_type_validation(self):
        """ Test error Type Validation """
        with self.assertRaises(TypeError):
            Square("3", 4)

    def test_size_value_validation(self):
        """ Test error Value Validation """
        with self.assertRaises(ValueError):
            Square(-2, 4)

    def test_height_type_validation(self):
        """ Test error Type Validation """
        with self.assertRaises(TypeError):
            Square(3, "4")

    def test_height_value_validation(self):
        """ Test error Value Validation """
        with self.assertRaises(ValueError):
            Square(2, -4)

    def test_x_type_validation(self):
        """ Test error Type Validation """
        with self.assertRaises(TypeError):
            Square(3, 4, "s")

    def test_x_value_validation(self):
        """ Test error Value Validation """
        with self.assertRaises(ValueError):
            Square(2, 4, -5)

    def test_y_type_validation(self):
        """ Test error Type Validation """
        with self.assertRaises(TypeError):
            Square(3, 4, '3')

    def test_y_value_validation(self):
        """ Test error Value Validation """
        with self.assertRaises(ValueError):
            Square(2, 4, -5)


class test_area_Square(unittest.TestCase):
    """ Test Function Araea """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_size_area(self):
        """ Test size area """
        s_test = Square(3)
        self.assertEqual(s_test.area(), 9)


class test_str_Square(unittest.TestCase):
    """ Test return str Function """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_str(self):
        """ Str Return """
        s_test = Square(5)
        self.assertEqual(str(s_test), "[Square] (1) 0/0 - 5")


class test_update_Square(unittest.TestCase):
    """ Testing Function Update Square """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_update_arg_void(self):
        """ Update void """
        s_test = Square(2, 10, 11, 12)
        s_test.update()
        self.assertEqual(s_test.size, 2)
        self.assertEqual(s_test.x, 10)
        self.assertEqual(s_test.y, 11)
        self.assertEqual(s_test.id, 12)

    def test_update_arg_id(self):
        """ Update id """
        s_test = Square(2, 10, 11, 12)
        s_test.update(89)
        self.assertEqual(s_test.size, 2)
        self.assertEqual(s_test.x, 10)
        self.assertEqual(s_test.y, 11)
        self.assertEqual(s_test.id, 89)

    def test_update_arg_size(self):
        """ Update size """
        s_test = Square(2, 10, 11, 12)
        s_test.update(89, 1)
        self.assertEqual(s_test.size, 1)
        self.assertEqual(s_test.x, 10)
        self.assertEqual(s_test.y, 11)
        self.assertEqual(s_test.id, 89)

    def test_update_arg_x(self):
        """ Update x """
        s_test = Square(2, 10, 11, 12)
        s_test.update(89, 1, 2, 3)
        self.assertEqual(s_test.size, 1)
        self.assertEqual(s_test.x, 2)
        self.assertEqual(s_test.y, 3)
        self.assertEqual(s_test.id, 89)

    def test_update_arg_y(self):
        """ Update y """
        s_test = Square(2, 10, 11)
        s_test.update(89, 1, 3, 4)
        self.assertEqual(s_test.size, 1)
        self.assertEqual(s_test.x, 3)
        self.assertEqual(s_test.y, 4)
        self.assertEqual(s_test.id, 89)

    def test_update_kwargs(self):
        """ Update Kwargs """
        s_test = Square(1, 2, 3, 4)
        s_test.update(id=10)
        self.assertEqual(s_test.id, 10)
        s_test.update(size=45)
        self.assertEqual(s_test.size, 45)
        s_test.update(x=90)
        self.assertEqual(s_test.x, 90)
        s_test.update(y=80)
        self.assertEqual(s_test.y, 80)


class test_dict_rectangle(unittest.TestCase):
    """ Test Dict Function """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_dict(self):
        """ Test Dict Represetation """
        s_test = Square(10, 2, 1, 9)
        s_test1 = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(s_test1, s_test.to_dictionary())
