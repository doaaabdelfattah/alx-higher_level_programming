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
        self.assertEqual(b5.id, 4)
        

if __name__ == "__main__":
    unittest.main()