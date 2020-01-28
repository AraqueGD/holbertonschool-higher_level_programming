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


class test_save_to_file(unittest.TestCase):
    """ Testing Function Save to File json """

    def test_save_to_file_one_rectangle(self):
        """ Test Save to File Json """
        r_test = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r_test])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)


class test_from_json_string(unittest.TestCase):
    """ Testing convert json to dictionary """

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))


class test_crate(unittest.TestCase):
    """ Testing Create Dictionary to Instance """

    def test_create_rectangle_original(self):
        r_test = Rectangle(3, 5, 1, 2, 7)
        r_test_dictionary = r_test.to_dictionary()
        r_test = Rectangle.create(**r_test_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r_test))


class test_load_from_file(unittest.TestCase):
    """ Testing Load From File """

    def test_load_from_file_first_rectangle(self):
        """ Test First rectangle """
        r_test = Rectangle(10, 7, 2, 8, 1)
        r_test2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r_test, r_test2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r_test), str(list_rectangles_output[0]))

    def test_load_from_file_square_types(self):
        """ Test Second rectangle """
        s_test = Square(5, 1, 3, 3)
        s_test2 = Square(9, 5, 2, 3)
        Square.save_to_file([s_test, s_test2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))


class test_save_to_file_csv(unittest.TestCase):
    """ Testing SAve to File csv """

    def test_save_to_file_csv_one_rectangle(self):
        """ Test save to file csv rectangle """
        r_test = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r_test])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())


class test_load_from_file_csv(unittest.TestCase):
    """ Testin load from file cvs """

    def test_load_from_file_csv_first_rectangle(self):
        r_test = Rectangle(10, 7, 2, 8, 1)
        r_test = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r_test, r_test])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r_test), str(list_rectangles_output[0]))


if __name__ == "__main__":
    unittest.main()
