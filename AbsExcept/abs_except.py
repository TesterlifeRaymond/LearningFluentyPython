"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/1/25 下午3:57
@File: abs_except.py
@License: MIT
"""

from collections import OrderedDict


class RequestDataSchema(OrderedDict):
    pass


def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            try:
                prepare = type(getattr(cls, key))
                if prepare is None:
                    assert prepare is None
                assert isinstance(prepare, type(value)),\
                    "TypeError: {} is must be {}". format(key, value)
            except CheckRequestExcept as err:
                print("[ AssertionError ]: {} attr ".format(cls.__name__), err)
        return cls
    return decorate


class TimeoutExcept(Exception):
    def __init__(self, msg):
        super(TimeoutExcept).__init__()


class CheckRequestExcept(Exception):
    def __init__(self, msg):
        super(CheckRequestExcept).__init__()


class BeforRequestMixin(type):

    def __new__(cls, name, bases, properties):
        for k, val in properties.__dict__.items():
            setattr(cls, k, val)
        return super().__new__(cls, name, bases, properties)

    @classmethod
    def __prepare__(cls, clsname, bases):
        schema = RequestDataSchema(**{
            "url": "testerlife.com",
            "body": {"a": 1, "b": 2},
            "json": None,
            "meta": [{"patch": "log.abc", "msg": "用户登录 log"}],
            "headers": None}
        )
        return schema


@check_attributes(
    url=str,
    body=dict,
    headers=dict,
    meta=list,
)
class Request(metaclass=BeforRequestMixin):
    pass


if __name__ == '__main__':
    print(Request.url)
    print(Request.body)
    print(Request.headers)
