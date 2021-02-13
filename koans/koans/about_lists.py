#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = []
        self.assertEqual(__, type(empty_list))
        self.assertEqual(__, len(empty_list))

    def test_list_literals(self):
        nums = []
        self.assertEqual(__, nums)

        nums[0:] = [1]
        self.assertEqual(__, nums)

        # use this as preferred way for appending to an existing list
        nums.append(333)
        self.assertListEqual([1, 333], nums)

        part_one = [1, 2]
        part_two = [3]
        all_parts = part_one + part_two

        self.assertListEqual(__, part_one)
        self.assertListEqual(__, part_two)
        self.assertListEqual(__, all_parts)


    def test_accessing_list_elements(self):
        noms = ["peanut", "butter", "and", "jelly"]

        self.assertEqual(__, noms[0])
        self.assertEqual(__, noms[3])
        self.assertEqual(__, noms[-1])
        self.assertEqual(__, noms[-3])

    def test_slicing_lists(self):
        noms = ["peanut", "butter", "and", "jelly"]

        self.assertEqual(__, noms[0:1])
        self.assertEqual(__, noms[0:2])
        self.assertEqual(__, noms[2:2])
        self.assertEqual(__, noms[2:20])
        self.assertEqual(__, noms[4:0])
        self.assertEqual(__, noms[4:100])
        self.assertEqual(__, noms[5:0])

    def test_slicing_to_the_edge(self):
        noms = ["peanut", "butter", "and", "jelly"]

        self.assertEqual(__, noms[2:])
        self.assertEqual(__, noms[:2])

    def test_lists_and_ranges(self):
        self.assertEqual(__, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        # observe list call
        self.assertEqual(__, list(range(5)))
        self.assertEqual(__, list(range(5, 9)))

    def test_ranges_with_steps(self):
        self.assertEqual(__, list(range(5, 3, -1)))
        self.assertEqual(__, list(range(0, 8, 2)))
        self.assertEqual(__, list(range(1, 8, 3)))
        self.assertEqual(__, list(range(5, -7, -4)))
        self.assertEqual(__, list(range(5, -8, -4)))

    def test_insertions(self):
        knight = ["you", "shall", "pass"]
        knight.insert(2, "not")
        self.assertEqual(__, knight)

        knight.insert(0, "Arthur")
        self.assertEqual(__, knight)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append("last")

        self.assertEqual(__, stack)

        popped_value = stack.pop()
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        popped_value = stack.pop(1)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append("last")

        self.assertEqual(__, queue)

        popped_value = queue.pop(0)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

    def test_sort_lists(self):
        numbers = [1, 3, 2, 9]

        # sort method does not return anything, but sorts in place
        self.assertEqual(__, numbers.sort())

        numbers = [1, 3, 2, 9]
        numbers.sort()
        self.assertEqual(__, numbers)

    def test_reverse_lists(self):
        numbers = [1, 3, 2, 9]

        # reverse method does not return anything, but sorts in place
        self.assertEqual(__, numbers.reverse())

        numbers = [1, 3, 2, 9]
        numbers.reverse()
        self.assertEqual(__, numbers)