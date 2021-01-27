#!/usr/bin/python3
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """dfg gdfgdfg dfdgdf"""

    def test_docstring(self):
        """dkf lkgfdgdf g"""
        self.assertIsNotNone(Base.__doc__)

    def test_a_init(self):
        """df dgdf gfd gdfgdfd"""
        t1 = Base()
        self.assertEqual(t1.id, 1)
        t2 = Base()
        self.assertEqual(t2.id, 2)

    def test_a_pasing_args(self):
        """df sfsdfsd fdsdsfds"""
        t1 = Base(15)
        self.assertEqual(t1.id, 15)
        t2 = Base(20)
        self.assertEqual(t2.id, 20)
        t3 = Base()
        self.assertEqual(t3.id, 3)
        t4 = Base(-5)
        self.assertEqual(t4.id, -5)
