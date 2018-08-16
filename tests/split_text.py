"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2017/12/7 上午10:41
@File: split_text.py
@License: MIT
"""
import json


class TestPythonClass:
    """ pass """
    def __init__(self):
        self.a = 1
        self.b = 2

    def __repr__(self):
        return json.dumps(self.__dict__)


if __name__ == '__main__':
    test = TestPythonClass()
    test_obj_dict = json.loads(repr(test))
    print(test_obj_dict)
