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

    def test_update_arg_void(self):
        """ Update void """
        r_test = Rectangle(2, 5, 10, 11, 12)
        r_test.update()
        self.assertEqual(r_test.width, 2)
        self.assertEqual(r_test.height, 5)
        self.assertEqual(r_test.x, 10)
        self.assertEqual(r_test.y, 11)
        self.assertEqual(r_test.id, 12)

    def test_update_arg_id(self):
        """ Update id """
        r_test = Rectangle(2, 5, 10, 11, 12)
        r_test.update(89)
        self.assertEqual(r_test.width, 2)
        self.assertEqual(r_test.height, 5)
        self.assertEqual(r_test.x, 10)
        self.assertEqual(r_test.y, 11)
        self.assertEqual(r_test.id, 89)

    def test_update_arg_width(self):
        """ Update width """
        r_test = Rectangle(2, 5, 10, 11, 12)
        r_test.update(89, 1)
        self.assertEqual(r_test.width, 1)
        self.assertEqual(r_test.height, 5)
        self.assertEqual(r_test.x, 10)
        self.assertEqual(r_test.y, 11)
        self.assertEqual(r_test.id, 89)

    def test_update_arg_height(self):
        """ Update height """
        r_test = Rectangle(2, 5, 10, 11, 12)
        r_test.update(89, 1, 2)
        self.assertEqual(r_test.width, 1)
        self.assertEqual(r_test.height, 2)
        self.assertEqual(r_test.x, 10)
        self.assertEqual(r_test.y, 11)
        self.assertEqual(r_test.id, 89)

    def test_update_arg_x(self):
        """ Update x """
        r_test = Rectangle(2, 5, 10, 11, 12)
        r_test.update(89, 1, 2, 3)
        self.assertEqual(r_test.width, 1)
        self.assertEqual(r_test.height, 2)
        self.assertEqual(r_test.x, 3)
        self.assertEqual(r_test.y, 11)
        self.assertEqual(r_test.id, 89)

    def test_update_arg_y(self):
        """ Update y """
        r_test = Rectangle(2, 5, 10, 11, 12)
        r_test.update(89, 1, 2, 3, 4)
        self.assertEqual(r_test.width, 1)
        self.assertEqual(r_test.height, 2)
        self.assertEqual(r_test.x, 3)
        self.assertEqual(r_test.y, 4)
        self.assertEqual(r_test.id, 89)

    def test_update_kwargs(self):
        """ Update Kwargs """
        r_test = Rectangle(1, 2, 3, 4, 5)
        r_test.update(id=10)
        self.assertEqual(r_test.id, 10)
        r_test.update(width=45)
        self.assertEqual(r_test.width, 45)
        r_test.update(height=67)
        self.assertEqual(r_test.height, 67)
        r_test.update(x=90)
        self.assertEqual(r_test.x, 90)
        r_test.update(y=80)
        self.assertEqual(r_test.y, 80)


if __name__ == "__main__":
    unittest.main()
