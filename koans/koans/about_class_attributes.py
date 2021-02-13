#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutClassMethods in the Ruby Koans
#

from runner.koan import *

class AboutClassAttributes(Koan):
    class Dog:
        pass

    def test_objects_are_objects(self):
        fido = self.Dog()
        self.assertEqual(__, isinstance(fido, object))

    def test_classes_are_types(self):
        self.assertEqual(__, self.Dog.__class__ == type)

    def test_classes_are_objects_too(self):
        self.assertEqual(__, issubclass(self.Dog, object))

    def test_creating_objects_without_defining_a_class(self):
        singularity = object()
        self.assertEqual(__, isinstance(singularity, object))

    def test_defining_attributes_on_individual_objects(self):
        fido = self.Dog()
        fido.legs = 4

        self.assertEqual(__, fido.legs)

    def test_defining_functions_on_individual_objects(self):
        # DO NOT use this in practice
        fido = self.Dog()
        fido.wag = lambda : 'fidos wag'

        self.assertEqual(__, fido.wag())

    def test_other_objects_are_not_affected_by_these_singleton_functions(self):
        fido = self.Dog()
        rover = self.Dog()

        # DO NOT use this in practice
        def wag():
            return 'fidos wag'
        fido.wag = wag

        with self.assertRaises(__): rover.wag()

    # ------------------------------------------------------------------

    class Dog2:
        def wag(self):
            return 'instance wag'

        def bark(self):
            return "instance bark"

        def growl(self):
            return "instance growl"

        @staticmethod
        def bark():
            return "staticmethod bark, arg: None"

        @classmethod
        def growl(cls):
            return "classmethod growl, arg: cls=" + cls.__name__

    def test_since_classes_are_objects_you_can_define_singleton_methods_on_them_too(self):
        self.assertRegex(self.Dog2.growl(), __)

    def test_classmethods_are_not_independent_of_instance_methods(self):
        fido = self.Dog2()
        self.assertRegex(fido.growl(), __)
        self.assertRegex(self.Dog2.growl(), __)

    def test_staticmethods_are_unbound_functions_housed_in_a_class(self):
        self.assertRegex(self.Dog2.bark(), __)

    def test_staticmethods_also_overshadow_instance_methods(self):
        fido = self.Dog2()
        self.assertRegex(fido.bark(), __)
        # DO NOT use same name for instance and class/static methods in practice
        # The actual execution will entirely depend on the order in which you specify the methods

    # ------------------------------------------------------------------

    class Dog3:
        def __init__(self):
            self._name = None

        def get_name_from_instance(self):
            return self._name

        def set_name_from_instance(self, name):
            self._name = name

        @classmethod
        def get_name(cls):
            return cls._name

        @classmethod
        def set_name(cls, name):
            cls._name = name


    def test_classes_and_instances_do_not_share_instance_attributes(self):
        fido = self.Dog3()
        fido.set_name_from_instance("Fido")
        fido.set_name("Rover")
        self.assertEqual(__, fido.get_name_from_instance())
        self.assertEqual(__, self.Dog3.get_name())

    def test_classes_and_instances_do_share_class_attributes(self):
        # DO NOT use class attributes except when it is really required e.g. configuration
        fido = self.Dog3()
        fido.set_name("Fido")
        self.assertEqual(__, fido.get_name())
        self.assertEqual(__, self.Dog3.get_name())
