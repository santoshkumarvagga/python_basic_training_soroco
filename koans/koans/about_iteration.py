#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutIteration(Koan):

    def test_iterators_are_a_type(self):
        it = iter(range(1,6))

        total = 0

        for num in it:
            total += num

        self.assertEqual(__, total)

    def test_iterating_with_next(self):
        stages = iter(['alpha','beta','gamma'])

        try:
            self.assertEqual(__, next(stages))
            next(stages)
            self.assertEqual(__, next(stages))
            next(stages)
        except StopIteration as ex:
            err_msg = 'Ran out of iterations'

        self.assertRegex(err_msg, __)

    # ------------------------------------------------------------------

    def add_ten(self, item):
        return item + 10

    def test_map_transforms_elements_of_a_list(self):
        seq = [1, 2, 3]
        mapped_seq = list()

        mapping = map(self.add_ten, seq)

        self.assertNotEqual(list, mapping.__class__)
        self.assertEqual(__, mapping.__class__)
        # In Python 3 built in iterator funcs return iterable view objects
        # instead of lists

        for item in mapping:
            mapped_seq.append(item)

        self.assertEqual(__, mapped_seq)

        # Note, iterator methods actually return objects of iter type in
        # python 3. In python 2 map() would give you a list.

    # list comprehension is usually cleaner than using map
    def test_comprehension_transforms_elements_of_a_list(self):
        seq = [1, 2, 3]
        mapped_seq = [self.add_ten(x) for x in seq]

        self.assertEqual(__, mapped_seq)

    def test_filter_selects_certain_items_from_a_list(self):
        def is_even(item):
            return (item % 2) == 0

        seq = [1, 2, 3, 4, 5, 6]
        even_numbers = list()

        for item in filter(is_even, seq):
            even_numbers.append(item)

        self.assertEqual(__, even_numbers)

    # Using list comprehension is usually cleaner than using filter
    def test_comprehension_selects_certain_items_from_a_list(self):
         def is_even(item):
              return (item % 2) == 0

         seq = [1, 2, 3, 4, 5, 6]
         even_numbers = [x for x in seq if is_even(x)]

         self.assertEqual(__, even_numbers)

    def test_just_return_first_item_found(self):
        def is_big_name(item):
            return len(item) > 4

        names = ["Jim", "Bill", "Clarence", "Doug", "Eli"]
        name = None

        iterator = filter(is_big_name, names)
        try:
            name = next(iterator)
        except StopIteration:
            msg = 'Ran out of big names'

        self.assertEqual(__, name)


    # ------------------------------------------------------------------

    def add(self,accum,item):
        return accum + item

    def multiply(self,accum,item):
        return accum * item

    def test_reduce_will_blow_your_mind(self):
        import functools
        # As of Python 3 reduce() has been demoted from a builtin function
        # to the functools module.

        result = functools.reduce(self.add, [2, 3, 4])
        self.assertEqual(__, result.__class__)
        # Reduce() syntax is same as Python 2

        self.assertEqual(__, result)

        result2 = functools.reduce(self.multiply, [2, 3, 4], 1)
        self.assertEqual(__, result2)

    # Usually explicit loop is usually cleaner, see https://www.artima.com/weblogs/viewpost.jsp?thread=98196
    def test_use_explicity_loop(self):

        result = sum([2, 3, 4])

        self.assertEqual(__, result)

        result2 = 1
        for i in [2, 3, 4]:
             result2 = self.multiply(result2, i)
        self.assertEqual(__, result2)

    # ------------------------------------------------------------------

    def test_use_pass_for_iterations_with_no_body(self):
        for num in range(1,5):
            pass

        self.assertEqual(__, num)

