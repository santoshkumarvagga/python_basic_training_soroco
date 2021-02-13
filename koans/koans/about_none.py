#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AboutNone(Koan):

    def test_none_is_an_object(self):
        # Unlike NULL in a lot of languages
        self.assertEqual(__, isinstance(None, object))

    def test_none_is_universal(self):
        # There is only one None
        # Use this as None check
        self.assertEqual(__, None is None)

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the block below.

        Don't worry about what 'try' and 'except' do, we'll talk about this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # What exception has been caught?
        self.assertEqual(__, ex2.__class__)

        # What message was attached to the exception?
        # (HINT: replace __ with part of the error message.)
        self.assertRegex(ex2.args[0], __)

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        # Use this as preferred way of comparison to None
        self.assertEqual(__, 0 is not None)
        self.assertEqual(__, False is not None)
        # Do not use "not 0 is None", see: https://www.python.org/dev/peps/pep-0008/#programming-recommendations
