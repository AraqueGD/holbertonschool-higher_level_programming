#!/usr/bin/python3
""" Unit Testing for Models/rectangle.py """

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """ Testing Rectangle Class """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_one_arg(self):
        """ Test in Rectangle receives one arg """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg(self):
        """ Test in Rectangle receives two arg """
        r_test = Rectangle(12, 2)
        self.assertEqual(r_test.id, 1)

    def test_three_arg(self):
        """ Test in Rectangle receives three arg """
        r_test = Rectangle(23, 4, 2)
        self.assertEqual(r_test.id, 1)

    def test_four_arg(self):
        """ Test in Rectangle receives four arg """
        r_test = Rectangle(13, 4, 9, 5)
        self.assertEqual(r_test.id, 1)

    def test_five_arg(self):
        """ Test in Rectangle receives five arg """
        r_test = Rectangle(23, 4, 6, 8, 10)
        self.assertEqual(r_test.id, 10)

    def test_None_arg(self):
        """ Test in Rectangle receives None arg """
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_Private_width(self):
        """ Test in Rectangle Acces for Private Attribute """
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 5, 6, 7).__width)

    def test_Private_height(self):
        """ Test in Rectangle Acces for Private Attribute """
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 5, 6, 7).__height)


class test_Raises_Validation(unittest.TestCase):
    """ Test width, height, x and y Validation """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_width_type_validation(self):
        """ Test error Type Validation """
        with self.assertRaises(TypeError):
            Rectangle("3", 4)

    def test_width_value_validation(self):
        """ Test error Value Validation """
        with self.assertRaises(ValueError):
            Rectangle(-2, 4)

    def test_height_type_validation(self):
        """ Test error Type Validation """
        with self.assertRaises(TypeError):
            Rectangle(3, "4")

    def test_height_value_validation(self):
        """ Test error Value Validation """
        with self.assertRaises(ValueError):
            Rectangle(2, -4)

    def test_x_type_validation(self):
        """ Test error Type Validation """
        with self.assertRaises(TypeError):
            Rectangle(3, 4, "s")

    def test_x_value_validation(self):
        """ Test error Value Validation """
        with self.assertRaises(ValueError):
            Rectangle(2, 4, -5)

    def test_y_type_validation(self):
        """ Test error Type Validation """
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 3, "8")

    def test_y_value_validation(self):
        """ Test error Value Validation """
        with self.assertRaises(ValueError):
            Rectangle(2, 4, 5, -8)


class test_area_rectangle(unittest.TestCase):
    """ Test Function Araea """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_width_area(self):
        """ Test width area """
        r_test = Rectangle(3, 4)
        self.assertEqual(r_test.area(), 12)

    def test_height_area(self):
        """ Test height area """
        r_test = Rectangle(3, 2)
        self.assertEqual(r_test.area(), 6)


class test_str_rectangle(unittest.TestCase):
    """ Test return str Function """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_str(self):
        """ Str Return """
        r_test = Rectangle(5, 5, 1)
        self.assertEqual(str(r_test), "[Rectangle] (1) 1/0 - 5/5")


class test_update_rectangle(unittest.TestCase):
    """ Testing Function Update Rectangle """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_update_none_arg(self):
        """ Test Update None arguments """
        r_test = Rectangle(10, 10, 10, 10)
        r_test.update(None)
        self.assertEqual(str(r_test), "[Rectangle] (2) 10/10 - 10/10")

    def test_update_one_arg(self):
        r_test = Rectangle(10, 10, 10, 10)
        r_test.update(89)
        self.assertEqual(str(r_test), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_arg(self):
        r_test = Rectangle(10, 10, 10, 10)
        r_test.update(89, 2)
        self.assertEqual(str(r_test), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_three_arg(self):
        r_test = Rectangle(10, 10, 10, 10)
        r_test.update(89, 2, 6)
        self.assertEqual(str(r_test), "[Rectangle] (89) 10/10 - 2/6")

    def test_update_four_arg(self):
        r_test = Rectangle(10, 10, 10, 10)
        r_test.update(89, 2, 6, 9)
        self.assertEqual(str(r_test), "[Rectangle] (89) 9/10 - 2/6")

    def test_update_five_arg(self):
        r_test = Rectangle(10, 10, 10, 10)
        r_test.update(89, 2, 6, 9, 7)
        self.assertEqual(str(r_test), "[Rectangle] (89) 9/7 - 2/6")


if __name__ == "__main__":
    unittest.main()
