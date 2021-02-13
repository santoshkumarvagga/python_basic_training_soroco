#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import logging
import traceback

class MySpecialError(RuntimeError):
    pass

class AboutExceptions(Koan):

    def test_exceptions_inherit_from_exception(self):
        mro = MySpecialError.mro()
        self.assertEqual(__, mro[1].__name__)
        self.assertEqual(__, mro[2].__name__)
        self.assertEqual(__, mro[3].__name__)
        self.assertEqual(__, mro[4].__name__)

    def test_try_clause(self):
        result = None
        try:
            # This is unittest method
            self.fail("Oops")
        except Exception as ex:
            result = 'exception handled'

            ex2 = ex

        self.assertEqual(__, result)

        self.assertEqual(__, isinstance(ex2, Exception))
        self.assertEqual(__, isinstance(ex2, RuntimeError))

        self.assertTrue(issubclass(RuntimeError, Exception), \
            "RuntimeError is a subclass of Exception")

        self.assertEqual(__, ex2.args[0])

    def test_raising_a_specific_error(self):
        result = None
        e = None
        try:
            raise MySpecialError("My Message")
        except MySpecialError as ex:
            result = 'exception handled'
            msg = ex.args[0]
            e = ex

        self.assertEqual(__, result)
        self.assertEqual(__, msg)

        # Raise exceptions with a descriptive message.
        self.assertEqual(__, str(e))

        # Prefer creating specific exception messages. Inherit at least from Exception class
        # If you are creating a library, consider creating a base library exception, and inherit all other exceptions
        # from the base library exception. See below for example

        class ShoeError(Exception):
            """Basic exception for errors raised by shoes"""

        class UntiedShoelace(ShoeError):
            """You could fall"""

        class WrongFoot(ShoeError):
            """When you try to wear your left show on your right foot"""

        # Inherit from builtin exception types when it makes sense
        class InvalidColor(ShoeError, ValueError):
            """When the color of the shoe is invalid"""

    def initialize_some_library(self):
        try:
            f = open("abc")
            # do more stuff
            f.close()
        except FileNotFoundError as ex:
            raise MySpecialError("Error while initialization") from ex

    def test_wrapping_exception(self):
        try:
            self.initialize_some_library()
        except MySpecialError as ex:
            msg = str(ex)

        # While creating libraries encapsulate internal exceptions into custom exception
        # Otherwise you may expose internal implementation to outside
        # and caller code will need to change if you change implementation
        self.assertEqual(__, msg)

    def test_log_exceptions(self):
        # Bad
        import traceback
        try:
            open("abc")
        except Exception as ex:
            pass

        # Good
        try:
            open("abc")
        except Exception as ex:
            msg = "Something bad happened: \n{traceback}".format(traceback=traceback.format_exc())
            logging.getLogger().error(msg)

        # Do not silently pass exceptions, at the minimum always log them the traceback and the exception
        # But also do not just log and throw the same exception, it will record multiple times the same exception
        self.assertRegex(msg, __)

    def handle_multiple_exceptions(self, input):
        try:
            if input == 1:
                raise ValueError("Wrong value")
            if input == 2:
                raise Exception("Something went wrong")
        except (ValueError, AttributeError) as ve:
            # Do something specific and handle
            return "This is handled"
        except Exception as ex:
            # Do something else
            msg = "Generic exception: {traceback}".format(traceback=traceback.format_exc())
            logging.getLogger().error(msg)
            return msg

    def test_multiple_excepts(self):
        # Have individual except block for each specific type of handling
        # Each except block can handle one or more exception type
        # Have specific exceptions handled first, and then handle generic exception like the base 'Exception'
        self.assertRegex(self.handle_multiple_exceptions(1), __)
        self.assertRegex(self.handle_multiple_exceptions(2), __)

    def test_else_clause(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = 'it broke'
            pass
        else:
            result = 'no damage done'

        # Avoid using else clause in try except in general
        self.assertEqual(__, result)

    def test_finally_clause(self):
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = 'always run'

        self.assertEqual(__, result)
        # use finally block to perform all the cleanups e.g. file close
