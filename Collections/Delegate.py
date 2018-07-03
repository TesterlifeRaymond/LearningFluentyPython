
# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.Delegate
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Delegate.py

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-07-03 15:35:41
"""


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name: str, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

    def __delattr__(self, name):
        if name.startswith("_"):
            super().__delattr__(name)
        else:
            delattr(self._obj, name)


class Demo:
    def __init__(self):
        self.foo = 10
        self.string = "Ray"
        self.city = "北京"

    def spam(self):
        return f"{self.string} in {self.city} {self.foo} years"


if __name__ == "__main__":
    proxy = Proxy(Demo())
    print(proxy.spam())
    print(proxy.foo)
    print(proxy.string)
    print(proxy.city)
    proxy.title = "demo"
    proxy.class_name = Proxy.__name__
    print(f"class {proxy.class_name} title is {proxy.title}")
    print(vars(proxy._obj))
    print(vars(proxy))
