#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTrueAndFalse(Koan):
    def truth_value(self, condition):
        if condition:
            return 'true stuff'
        else:
            return 'false stuff'

    def test_true_is_treated_as_true(self):
        self.assertEqual(__, self.truth_value(True))

    def test_false_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(False))

    def test_none_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(None))

        # it is better to explicity test for None
        a = None
        self.assertEqual(__, self.truth_value(a is None))

    def test_zero_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(0))

    def test_empty_collections_are_treated_as_false(self):
        # It is more pythonic to test for empty sequences directly, rather than using len
        # See https://www.python.org/dev/peps/pep-0008/#programming-recommendations
        self.assertEqual(__, self.truth_value([]))
        self.assertEqual(__, self.truth_value(()))
        self.assertEqual(__, self.truth_value({}))
        self.assertEqual(__, self.truth_value(set()))

    def test_blank_strings_are_treated_as_false(self):
        # It is more pythonic to test for empty sequences directly, rather than using len
        # See https://www.python.org/dev/peps/pep-0008/#programming-recommendations
        self.assertEqual(__, self.truth_value(""))

    def test_everything_else_is_treated_as_true(self):
        self.assertEqual(__, self.truth_value(1))
        self.assertEqual(__, self.truth_value([0]))
        self.assertEqual(__, self.truth_value((0,)))
        self.assertEqual(__,
            self.truth_value("Python is named after Monty Python"))
        self.assertEqual(__, self.truth_value(' '))
        self.assertEqual(__, self.truth_value('0'))
