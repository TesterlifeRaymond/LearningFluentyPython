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

ENUM = (int, dict, list, tuple, str, set, type)


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
            if len(args) > 0:
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
            if isinstance(value, classmethod):
                wrap_properties[key] = classmethod(log(value.__func__))
            elif isinstance(value, staticmethod):
                wrap_properties[key] = staticmethod(log(value.__func__))
            elif key.startswith('__') or isinstance(value, property):
                wrap_properties[key] = value
            else:
                wrap_properties[key] = log(value)
        properties.update(**wrap_properties)
        return type.__new__(mcs, name, bases, properties)


class TestMetaLogger(metaclass=LoggerMeta):
    def __init__(self):
        self.index = 1
        self.end = 10

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
    
    @classmethod
    def test_ddd_log(cls):
        return 222
    
    @property
    def test_property(self):
        return self.end


if __name__ == '__main__':
    instance = TestMetaLogger()
    TestMetaLogger.test_func_log(7, 8)
    TestMetaLogger.test_bbb_log(9, 10)
    instance.test_aaa_log(1, 2)
    instance.test_func_log(3, 4)
    instance.test_bbb_log(5, 6)
    TestMetaLogger.test_ccc_log()
    instance.test_ccc_log()
    TestMetaLogger.test_ddd_log()
    instance.test_ddd_log()
    print(instance.test_property)
