#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        # In raw strings, backlashes have no special meaning as an escape character
        # Use raw strings for file paths, regex, read more at https://knowledge.kitchen/Raw_strings_in_Python
        string = "Hello, world."
        self.assertEqual(__, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(__, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(__, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(__, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        # In raw strings, backlashes have no special meaning as an escape character
        # Use raw strings for file paths, regex, read more at https://knowledge.kitchen/Raw_strings_in_Python
        string = r"Konnichi wa, world!"
        self.assertEqual(__, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual(__, string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual(__, string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(__, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        # use repr to see raw representation of a string: print (repr(string))
        # NOTE: Instead of just putting the integer, use len(<one-line-string-representation>) in assert statement
        self.assertEqual(__, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        self.assertEqual(__, len(string))

    def test_use_separate_string_on_each_line(self):
        # use this as preferred way of creating multi-line strings
        # Refer https://mail.python.org/pipermail/python-list/2013-November/661385.html
        # Not there are no commas (it's not a tuple)
        # As best practice have whitespaces at the start of the line, where it is easier to verify
        string = ("It was the best of times,"
                  " It was the worst of times.")
        self.assertEqual(__, len(string))

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual(__, string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual(__, string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual(__, hi)
        self.assertEqual(__, there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual(__, hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual(__, original)

    def test_join_for_multiple_string_concatenation(self):
        # use join for multiple string concatenation
        strings = ["Hello,", "how", "are", "you"]
        string_without_space = ''.join(strings)
        string_with_space = ' '.join(strings)
        self.assertEqual(__, string_with_space)
        self.assertEqual(__, string_without_space)

    def test_format_string(self):
        # Use format for creating formatted strings instead of string concatenation
        # This is useful in, for example, generating log messages
        name = "Bob"
        string = "Hello, {name}, how are you".format(name=name)
        self.assertEqual(__, string)
