
# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.StructTuple
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    StructTuple.py

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-07-09 16:34:59
"""
import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError(f"{len(cls._fields)} arguments required .")
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ["name", "shares", "prices"]


class Point(StructTuple):
    _fields = ["x", "y"]


if __name__ == "__main__":
    # print(signature(Point))
    # print(signature(Stock))
    s = Stock("ACME", 50, 91.1)
    print(s)
    print(s.name, s.prices)
