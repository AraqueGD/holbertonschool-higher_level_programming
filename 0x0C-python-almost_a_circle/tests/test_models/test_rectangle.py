#!/usr/bin/python3
""" Unit Testing for Models/rectangle.py """

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """ Testing Rectangle Class """

    def test_one_arg(self):
        """ Test in Rectangle receives one arg """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg(self):
        """ Test in Rectangle receives two arg """
        r2 = Rectangle(12, 2)
        r3 = Rectangle(10, 2)
        self.assertEqual(r2.id, r3.id - 1)

    def test_three_arg(self):
        """ Test in Rectangle receives three arg """
        r4 = Rectangle(23, 4, 2)
        r5 = Rectangle(10, 2, 5)
        self.assertEqual(r4.id, r5.id - 1)

    def test_four_arg(self):
        """ Test in Rectangle receives four arg """
        r4 = Rectangle(13, 4, 9, 5)
        self.assertEqual(r4.id, 4)

    def test_five_arg(self):
        """ Test in Rectangle receives five arg """
        r5 = Rectangle(23, 4, 6, 8, 10)
        self.assertEqual(r5.id, 10)

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


if __name__ == "__main__":
    unittest.main()
