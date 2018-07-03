# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.SortedItem
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    SortedItem.py

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-07-03 10:55:17
"""
import collections
from collections import Sequence
import bisect


class SortedItem(Sequence):
    def __init__(self, item=None):
        self._item = sorted(item) if item is not None else []

    def __getitem__(self, index):
        return self._item[index]

    def __len__(self):
        return len(self._item)

    def add(self, item):
        bisect.insort(self._item, item)


class Item(collections.MutableSequence):
    def __init__(self, initial=None):
        self._item = list(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._item[index]

    def __setitem__(self, index, value):
        self._item[index] = value

    def __delitem__(self, index):
        del self._item[index]

    def insert(self, index, value):
        self._item.insert(index, value)

    def __len__(self):
        return len(self._item)


if __name__ == "__main__":
    item = SortedItem([4, 3, 55, 1, 52, 66, 7])
    print(list(item))
