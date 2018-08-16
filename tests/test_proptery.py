# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.test_proptery
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    learning python cookbook

    :copyright: (c) 2018 by  Raymond.
    :license: LICENSE_NAME, see LICENSE for more details.
    :last modified by 2018-07-02 16:38:38
"""

import math


def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            try:
                assert type(getattr(cls, key)) is value,\
                    "TypeError: {} is must be {}". format(key, value)
            except AssertionError as err:
                print("[ AssertionError ]: {} attr ".format(cls.__name__), err)
        return cls
    return decorate


@check_attributes(
    name=str,
    age=int
)
class CheckString:
    name = "Ray"
    age = "10"


class LazyProperty:
    def __init__(self, func):
        """
        init LazyProperty
        @func: func or method
        """
        self.func = func

    def __get__(self, instance, cls):
        """
        descriptor prot
        """
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius ** 2


class Data:
    """ data struct """
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


if __name__ == "__main__":
    data = Data("Ray", 20, "北京")
    print(type(vars(data)), vars(data))

    circle = Circle(4.0)
    print(circle.area)
    circle.radius = 15.0
    print(circle.area)
