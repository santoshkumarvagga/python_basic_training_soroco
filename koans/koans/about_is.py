#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This Koan will try to explain possible pitfalls that can happen when using "is"
#

from runner.koan import *


class AboutIs(Koan):

    def test_is_is_not_what_it_is(self):
        # Be careful when you use "is". "is" compares ID's of objects. Every instance will have different ID.
        # Use "==" when you have to compare values.
        # Every empty list has a different id
        self.assertEqual(__, [] is [])
        self.assertEqual(__, [] == [])

    def test_using_not(self):
        # Be careful when you use "not" with "is"
        self.assertEqual(__, "This" is not None)
        self.assertEqual(__, "This" is (not None))

    def test_object_interning(self):
        # Python has a feature of object interning. When you want to create multiple copies of immutable objects,
        # python can create one object and point everything else to the same object. And also it doesn't have to
        # worry as the object is immutable.
        a = 257
        b = 257
        self.assertEqual(__, a is b)

        # Mostly interning is done during bytecode compilation, Hence the following statements will not be interned
        a = 257 * 1
        b = 257 * 1
        self.assertEqual(__, a is b)

    def test_using_none(self):
        # There is only one none object in python, hence you can safely use is when comparing for None
        # It is actually preferred to use "is None"
        self.assertEqual(__, None is None)
        self.assertEqual(__, id(None) == id(None))

    def test_using_booleans(self):
        # Similar to None, you will have a single stable object for True and False throughout your python instance
        self.assertEqual(__, id(True) == id(True))

        # When using booleans, always try to prefer using them directly without any comparisions.
        self.assertEqual(__, 1 is True)
        self.assertEqual(__, 1)
        self.assertEqual(__, 1 == True)
