"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/10 下午3:34
@File: MetaClass.py
@License: MIT
"""

import logging
from functools import wraps

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def log(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if isinstance(func, staticmethod):
            args = args[1::]
            func_name = func.__func__.__name__
            result = func.__func__(*args, **kwargs)
        elif isinstance(func, classmethod):
            func_name = func.__func__.__name__
            result = func.__func__(*args, **kwargs)
        else:
            func_name = func.__name__
            result = func(*args, **kwargs)
        logger.info("[ Func {} Called ]".format(func_name))
        logger.info("[ Func Paramter ]: Args: {}, Kwargs: {}".format(args, kwargs))
        logger.info("[ Func Result ]: {}({}, {})".format(func_name, args, kwargs))
        return result
    return wrap


class LoggerMeta(type):

    def __new__(mcs, name, bases, properties):
        wrap_properties = {}
        for key, value in properties.items():
            if isinstance(value, (classmethod, staticmethod)):
                wrap_properties[key] = log(value.__func__)
            if key.startswith('__'):
                wrap_properties[key] = value
            else:
                wrap_properties[key] = log(value)
        properties.update(**wrap_properties)
        return type.__new__(mcs, name, bases, properties)


class TestMetaLogger(metaclass=LoggerMeta):
    @staticmethod
    def test_func_log(a, b):
        return a, b
    
    def test_aaa_log(self, a, b):
        return a, b

    @classmethod
    def test_bbb_log(cls, a, b):
        return a, b


if __name__ == '__main__':
    instance = TestMetaLogger()
    print(instance.test_aaa_log(1, 2))
    print(instance.test_func_log(3, 4))
    print(instance.test_bbb_log(5, 6))
