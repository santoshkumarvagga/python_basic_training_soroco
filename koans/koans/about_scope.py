#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

from . import jims
from . import joes

counter = 0 # Global

class AboutScope(Koan):
    #
    # NOTE:
    #   Look in jims.py and joes.py to see definitions of Dog used
    #   for this set of tests
    #

    def test_dog_is_not_available_in_the_current_scope(self):
        with self.assertRaises(__): fido = Dog()

    def test_you_can_reference_nested_classes_using_the_scope_operator(self):
        fido = jims.Dog()
        # name 'jims' module name is taken from jims.py filename

        rover = joes.Dog()
        self.assertEqual(__, fido.identify())
        self.assertEqual(__, rover.identify())

        self.assertEqual(__, type(fido) == type(rover))
        self.assertEqual(__, jims.Dog == joes.Dog)

    # ------------------------------------------------------------------

    class str:
        pass

    def test_bare_bones_class_names_do_not_assume_the_current_scope(self):
        # It is never a good idea to name your classes or methods same as standard ones
        self.assertEqual(__, AboutScope.str == str)

    def test_nested_string_is_not_the_same_as_the_system_string(self):
        self.assertEqual(__, self.str == type("HI"))

    def test_str_without_self_prefix_stays_in_the_global_scope(self):
        self.assertEqual(__, str == type("HI"))

    # ------------------------------------------------------------------

    PI = 3.1416

    def test_constants_are_defined_with_an_initial_uppercase_letter(self):
        self.assertAlmostEqual(3.1416, self.PI)
        # Note, floating point numbers in python are not precise.
        # assertAlmostEqual will check that it is 'close enough'

    def test_constants_are_assumed_by_convention_only(self):
        self.PI = "rhubarb"
        self.assertEqual(__, self.PI)
        # There aren't any real constants in python. Its up to the developer
        # to keep to the convention and not modify them.

    # ------------------------------------------------------------------

    def increment_using_local_counter(self):
        # This creates a new local variable
        # Ideally do not attempt to modify a global variable
        counter = 2

    def increment_using_global_counter(self):
        global counter
        counter = 3

    def test_accessing_global_counter(self):
        global counter
        self.assertEqual(__, counter == 0)

    def test_accessing_global_counter_without_global(self):
        # Can be accessed without global keyword
        self.assertEqual(__, counter == 0)

    def test_incrementing_with_local_counter(self):
        global counter
        self.increment_using_local_counter()
        self.assertEqual(__, counter == 2)

    def test_incrementing_with_global_counter(self):
        global counter
        self.increment_using_global_counter()
        self.assertEqual(__, counter == 3)

    # Avoid using global keyword, it is not clean and makes debugging difficult


    # ------------------------------------------------------------------

    global deadly_bingo
    deadly_bingo = [4, 8, 15, 16, 23, 42]

    def test_global_attributes_can_be_created_in_the_middle_of_a_class(self):
        self.assertEqual(__, deadly_bingo[5])
