
# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.MultiMethod
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    MultiMethod.py

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-07-10 11:25:43
"""

import inspect
import types


class MultiMethod:
    """
    Represents a single multimethod
    """
    def __init__(self, name):
        self._method = []
        self.__name__ = name

    def register(self, meth):
        """
        Register a new method as multimethod
        """
        sig = inspect.signature(meth)

        _types = []
        for name, param in sig.parameters.items():
            if name == "self":
                continue
            if param.annotation is inspect.Parameter.empty():
                raise TypeError(f"Argument {name} must"
                                "be annotated with a type")
            if not isinstance(param.annotation, type):
                raise TypeError(f"Argument {name} must"
                                "be annotated with a type")
            if param.default is not inspect.Parameter.empty():
                self._method[tuple(_types)] = meth
            types.append(param.annotation)

        self._method[tuple(_types)] = meth

    def __call__(self, *args):
        _types = tuple(type(arg) for arg in args[1:])
        meth = self._method.get(_types, None)

        if meth:
            return meth(*args)
        else:
            raise TypeError(" not matching method for types")
