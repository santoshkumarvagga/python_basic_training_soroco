#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based slightly on the lambdas section of AboutBlocks in the Ruby Koans
#

from runner.koan import *

class AboutLambdas(Koan):
    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        add_one = lambda n: n + 1
        self.assertEqual(__, add_one(10))

    # ------------------------------------------------------------------

    def make_order(self, order):
        return lambda qty: str(qty) + " " + order + "s"

    def test_accessing_lambda_via_assignment(self):
        sausages = self.make_order('sausage')
        eggs = self.make_order('egg')

        self.assertEqual(__, sausages(3))
        self.assertEqual(__, eggs(2))

    def test_accessing_lambda_without_assignment(self):
        self.assertEqual(__, self.make_order('spam')(39823))

    def test_lambdas_can_be_difficult_to_trace(self):
        # Avoid
        # The resulting function object is '<lambda>', thus making it difficult
        # to check in tracebacks and string representation
        square = lambda x : x ** x

        self.assertEqual(__, square.__name__)

        # Better
        # Lambda's are better suited for callback functions, however generally avoid lambda usage
        # unless you are really into a bind.
        def process(x, fn):
            return fn(x)

        self.assertEqual(__, process(4, fn = lambda x : x + 10))

        # Prefer
        # This way of definition explicitly assigns 'square' as the name
        # thus making debugging easier
        def square(x): return x ** x

        self.assertEqual(__, square.__name__)
    
    # In general, do *NOT* use lambdas unless you know what you are doing.
