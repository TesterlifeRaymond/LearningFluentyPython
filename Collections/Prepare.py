
# -*- coding: utf-8 -*-
"""
    LearningFluentyPython.Prepare
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Prepare.py

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-07-09 15:07:44
"""

from collections import OrderedDict
from inspect import Signature, Parameter, signature


class Prepare:
    def __new__(cls, name, bases, bdict):
        bdict = OrderedDict(**bdict)
        return type(name, bases, bdict)

    @classmethod
    def __prepare__(cls, clsname, bases):
        """
        该特殊方法在类定义一开始的时候立刻得到盗用, 调用时以类名和基类
        名称作为参数吗他必须返回一个映射型对象(mapping object) 供处理
        类定义时使用
        """
        result = OrderedDict(clsname=clsname, bases=bases)
        return result


class NewInstance(metaclass=Prepare):
    def __init__(self, *args):
        self.args = args


def make_sign(*args):
    param = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in args]
    return Signature(param)


class Structure:
    __signature__ = make_sign()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for key, value in bound_values.arguments.items():
            setattr(self, key, value)


class Stock(Structure):
    __signature__ = make_sign("name", "share", "age")


class StructureMeta(type):
    # or mixin class
    # 通过定义元类, 在类创建的同时增加__signature__属性, 并绑定_fields
    # 的全部指定信息
    def __new__(cls, clsname, bases, clsdict):
        clsdict["__signature__"] = make_sign(*clsdict.get("_fields", []))
        return super().__new__(cls, clsname, bases, clsdict)


class User(metaclass=StructureMeta):
    _fields = ("name", "city", "age")


class Student(metaclass=StructureMeta):
    _fields = ("counter", "classname", "subject")


if __name__ == "__main__":
    print(signature(User))
    print(signature(Student))
    # print(signature(Stock))
    # prepare = NewInstance([1, 5, 12, 2, 3, 55, 13, 25])
    # print(prepare)
