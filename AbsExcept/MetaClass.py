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

ENUM = (int, dict, list, tuple, str)


def log(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if isinstance(func, staticmethod):
            if len(args) > 0:
                args = args[1::] if not isinstance(args[0], ENUM) else args
            func_name = func.__func__.__name__
            result = func.__func__(*args, **kwargs)
        elif isinstance(func, classmethod):
            _args = [func.__class__]
            if len(args) > 1:
                args = args[1::] if not isinstance(args[0], ENUM) else args
            _args.extend(list(args))
            func_name = func.__func__.__name__
            result = func.__func__(*_args, **kwargs)
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
    
    @staticmethod
    def test_ccc_log():
        return 111


if __name__ == '__main__':
    instance = TestMetaLogger()
    print(TestMetaLogger.test_func_log(7, 8))
    print(TestMetaLogger.test_bbb_log(9, 10))
    print(instance.test_aaa_log(1, 2))
    print(instance.test_func_log(3, 4))
    print(instance.test_bbb_log(5, 6))
    print(TestMetaLogger.test_ccc_log())
    print(instance.test_ccc_log())
