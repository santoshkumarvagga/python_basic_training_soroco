#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMethods in the Ruby Koans
#

from runner.koan import *

def my_global_function(a,b):
    return a + b

class AboutMethods(Koan):
    def test_calling_a_global_function(self):
        self.assertEqual(__, my_global_function(2,3))

    # NOTE: Wrong number of arguments is not a SYNTAX error, but a
    # runtime error.
    def test_calling_functions_with_wrong_number_of_arguments(self):
        try:
            my_global_function()
        except TypeError as exception:
            msg = exception.args[0]

        # Note, the text comparison works for Python 3.2
        # It has changed in the past and may change in the future
        self.assertRegex(msg,
            r'my_global_function\(\) missing 2 required positional arguments')

        try:
            my_global_function(1, 2, 3)
        except Exception as e:
            msg = e.args[0]

        # Note, watch out for parenthesis. They need slashes in front!
        self.assertRegex(msg, __)

    # ------------------------------------------------------------------

    def pointless_method(self, a, b):
        sum = a + b

    def test_which_does_not_return_anything(self):
        self.assertEqual(__, self.pointless_method(1, 2))
        # Notice that methods accessed from class scope do not require
        # you to pass the first "self" argument?

    def test_named_arguments_are_cleaner(self):
        # Prefer named arguments in method call
        self.assertEqual(__, self.pointless_method(a=1, b=2))
    # ------------------------------------------------------------------

    def method_with_defaults(self, a, b='default_value'):
        return [a, b]

    def test_calling_with_default_values(self):
        self.assertEqual(__, self.method_with_defaults(1))
        self.assertEqual(__, self.method_with_defaults(1, 2))

    def method_with_mutable_defaults(self, a, b=[]):
        b.append(a)
        return b

    def test_donot_use_mutable_data_for_default_values(self):
        self.assertEqual(__, self.method_with_mutable_defaults(1))
        # Bad
        self.assertEqual(__, self.method_with_mutable_defaults(2))


    def method_with_immutable_defaults(self, a, b=None):
        if b is None:
            b = []
        b.append(a)
        return b

    def test_use_immutable_data_for_default_values(self):
        self.assertEqual(__, self.method_with_immutable_defaults(1))
        # Good
        self.assertEqual(__, self.method_with_immutable_defaults(2))

    # ------------------------------------------------------------------

    def method_with_var_args(self, *args):
        return args

    def test_calling_with_variable_arguments(self):
        self.assertEqual(__, self.method_with_var_args().__class__)
        self.assertEqual(__, self.method_with_var_args())
        self.assertEqual(__, self.method_with_var_args('one'))
        self.assertEqual(__, self.method_with_var_args('one', 'two'))

    def method_with_var_args_kwargs(self, *args, **kwargs):
        return kwargs

    def test_calling_with_variable_arguments_kwargs(self):
        self.assertEqual(__, self.method_with_var_args_kwargs().__class__)
        self.assertEqual(__, self.method_with_var_args_kwargs())
        self.assertEqual(__, self.method_with_var_args_kwargs(one=1))
        self.assertEqual(__, self.method_with_var_args_kwargs('one', 'two'))
    # ------------------------------------------------------------------

    def function_with_the_same_name(self, a, b):
        return a + b

    def test_functions_without_self_arg_are_global_functions(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(__, function_with_the_same_name(3,4))

    def test_calling_methods_in_same_class_with_explicit_receiver(self):
        def function_with_the_same_name(a, b):
            return a * b

        # Functions with same name are good to know about, but very bad to use in practice
        self.assertEqual(__, self.function_with_the_same_name(3,4))

    # ------------------------------------------------------------------

    def another_method_with_the_same_name(self):
        return 10

    link_to_overlapped_method = another_method_with_the_same_name

    def another_method_with_the_same_name(self):
        return 42

    def test_that_old_methods_are_hidden_by_redefinitions(self):
        self.assertEqual(__, self.another_method_with_the_same_name())

    def test_that_overlapped_method_is_still_there(self):
        self.assertEqual(__, self.link_to_overlapped_method())

    # ------------------------------------------------------------------

    def empty_method(self):
        pass

    def test_methods_that_do_nothing_need_to_use_pass_as_a_filler(self):
        self.assertEqual(__, self.empty_method())

    def test_pass_does_nothing_at_all(self):
        "You"
        "shall"
        "not"
        pass
        self.assertEqual(__, "Still got to this line" != None)

    # ------------------------------------------------------------------

    def one_line_method(self): return 'Madagascar'

    def test_no_indentation_required_for_one_line_statement_bodies(self):
        self.assertEqual(__, self.one_line_method())

    # ------------------------------------------------------------------

    def method_with_documentation(self):
        "A string placed at the beginning of a function is used for documentation"
        return "ok"

    def test_the_documentation_can_be_viewed_with_the_doc_method(self):
        self.assertRegex(self.method_with_documentation.__doc__,
                         "A string placed at the beginning of a function is used for documentation")

    # ------------------------------------------------------------------

    class Dog:
        def name(self):
            return "Fido"

        def _tail(self):
            # Prefixing a method with an underscore implies private scope
            return "wagging"

        def __password(self):
            return 'password' # Genius!

    def test_calling_methods_in_other_objects(self):
        rover = self.Dog()
        self.assertEqual(__, rover.name())

    def test_private_access_is_implied_but_not_enforced(self):
        rover = self.Dog()

        # In most of the cases you would not want to access the private attributes or method of a class outside
        # This is a little rude, but legal
        self.assertEqual(__, rover._tail())

    def test_attributes_with_double_underscore_prefixes_are_subject_to_name_mangling(self):
        rover = self.Dog()
        with self.assertRaises(__): password = rover.__password()

        # But this still is!
        self.assertEqual(__, rover._Dog__password())

        # Name mangling exists to avoid name clash issues when subclassing.
        # It is not for providing effective access protection

    # ------------------------------------------------------------------
    def method_with_multiple_return_types(self, val):
        if val == 1:
            return True
        return str(val)

    def test_method_donot_use_multiple_return_types(self):
        # Bad, return type changes with input
        call1 = self.method_with_multiple_return_types(1)
        call2 = self.method_with_multiple_return_types(2)

        self.assertEqual(__, isinstance(call1, bool))
        self.assertEqual(__, isinstance(call2, bool))

        # Always return a consistent return type
        # For missing values consider returning None e.g. find_something() may return None
        # For collections, it might be better to return empty collection find_all() may return [] but not None
        # Raise exceptions for errors, e.g. do_something() should raise Exception on failure and not return True/ False
        # For checks, it might be ok to return boolean, e.g. is_this_ok() can return True or  False

    # ------------------------------------------------------------------

    def method_returns_multiple_vals(self):
        return "one", 1

    def method_returns_multiple_vals_using_namedtuples(self):
        # Tuple defined inside the method just for convenience
        import collections
        number = collections.namedtuple('number', ["string", "value"])
        return number(string="one", value=1)

    def test_method_with_multiple_return_values(self):
        # tuples are commonly used
        a, b = self.method_returns_multiple_vals()

        self.assertEqual(__, a)
        self.assertEqual(__, b)

        # Usually namedtuple or dict or object are cleaner for multi value returns
        num = self.method_returns_multiple_vals_using_namedtuples()
        self.assertEqual(__, num.string)
        self.assertEqual(__, num.value)