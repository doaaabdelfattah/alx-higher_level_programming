#!/usr/bin/python3
# test_base.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines unittests for base.py.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTestCase(unittest.TestCase):
    """Unittests for the Base class."""

        
    def test_base_task1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        
        b4 = Base(7)
        self.assertEqual(b4.id, 7)
        b5 = Base()
        self.assertEqual(b1.id, 4)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)


if __name__ == "__main__":
    unittest.main()