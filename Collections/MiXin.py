
# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.MiXin
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    MiXin.py

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-07-03 16:10:35
"""
import json
from collections import OrderedDict


class LoggerMappingMixin(dict):
    __slots__ = ()

    def __getitem__(self, name):
        print(f"getting dict key: {name}")
        return super().__getitem__(name)

    def __setitem__(self, key, value):
        print(f"setting dict key and value: {key}, {value}")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        print(f"deleting key: {key}")
        super().__delitem__(key)


class SetOnceMappingMixin:
    def __setitem__(self, key, value):
        if key in self:
            print(f"{key} is already in self")
        else:
            super().__setitem__(key, value)


class ProjectDict(LoggerMappingMixin):
    pass


class ProjectOnceDict(SetOnceMappingMixin, OrderedDict):
    pass


if __name__ == "__main__":
    once = ProjectOnceDict()
    once["z"] = 3
    once["x"] = 1
    once["y"] = 2
    print(json.dumps(once, indent=4))
    print(ProjectDict.mro())
    d = ProjectDict()
    d['city'] = "北京"
    print(d["city"])
    d["user"] = "Ray"
    print(d["user"])
    d["age"] = 30
    print(d)
