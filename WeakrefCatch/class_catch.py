
# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.class_catch
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Catched class instance

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-07-05 15:23:09
"""
import types
from inspect import getargspec, signature
from functools import wraps
from weakref import WeakValueDictionary


class Spam(object):
    _catched = WeakValueDictionary()

    """Docstring for Spam. 这种方式, 会每次调用__init__方法"""

    def __new__(cls, name):
        if name in cls._catched:
            return cls._catched[name]
        else:
            self = super().__new__(cls)
            cls._catched[name] = self
            return self

    def __init__(self, name):
        """TODO: to be defined1. """
        print("Initial Spam class")
        self.name = name


class SpamManagerCatched:
    def __init__(self):
        self._catched = WeakValueDictionary()
        self.name = None

    def _get_spam(self, name):
        self.name = name

        if name in self._catched:
            return self._catched[name]
        else:
            obj = SpamManager(name)
            self._catched[name] = obj
            return obj

    def _clear(self):
        self._catched.clear()

    def __repr__(self):
        return self.name


class InstanceNcalls:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


class SpamManager:
    manager = SpamManagerCatched()

    def __init__(self, name):
        self.name = name

    @property
    def get_spam(self):
        return SpamManager.manager._get_spam(self.name)

    @InstanceNcalls
    def bar(self, x, y):
        return x - y


@InstanceNcalls
def add(x, y):
    return x + y


def params(x, y, z=None):
    pass


if __name__ == "__main__":
    print(getargspec(params).args)
    print(signature(params))
    # spam_data_one = SpamManager("Ray").get_spam
    # spam_data_two = SpamManager("Raymond").get_spam
    # spam_data_three = SpamManager("Ray").get_spam
    # print(spam_data_one is spam_data_three)
    # print(spam_data_one is spam_data_two)
    print(add(1, 2), add(3, 55), add(4, 12))
    print(add.ncalls)
    # print(add(5, 55), add.ncalls)
    # spam_data_one.bar(10, 6)
    # spam_data_three.bar(55, 23)
    # spam_data_two.bar(12, 12)
    # print(spam_data_one.bar.ncalls)
    # print(spam_data_two.bar.ncalls)
    # print(spam_data_three.bar.ncalls)
    # print(SpamManager("Ray").get_spam is SpamManager("Ray").get_spam)
