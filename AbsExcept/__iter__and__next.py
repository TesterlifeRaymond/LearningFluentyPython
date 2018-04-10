"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/10 下午6:09
@File: __iter__and__next.py.py
@License: MIT
"""


class TestIter:
    def __init__(self, num):
        self.data = list(range(1, num))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.data) == 0:
            raise StopIteration
        return self.data.pop()


if __name__ == '__main__':
    for item in TestIter(10):
        print(item)
