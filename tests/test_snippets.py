"""
@File: test_snippets
@Author: Ray
@Date: 2018-01-29 14:31:52
@Version: 1.0
"""


class X(object):

    def __get__(self, obj, type=None):
        return 0

    def __set__(self, obj, value):
        pass


class Y(object):
    x = X()


y = Y()
y.__dict__['x'] = 1

print(dir(y))
print(vars(y))

print(y.x)
assert y.x == 0
