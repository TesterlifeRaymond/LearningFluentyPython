"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/1/25 下午3:57
@File: abs_except.py
@License: MIT
"""


class TimeoutExcept(Exception):
    def __init__(self, msg):
        super(TimeoutExcept).__init__()


if __name__ == '__main__':
    try:
        raise TimeoutExcept("连接超时")
    except TimeoutExcept as err:
        print(err)
