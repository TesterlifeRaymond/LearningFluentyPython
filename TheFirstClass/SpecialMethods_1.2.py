"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2017/11/28 下午4:56
@File: SpecialMethods_1.2.py
@License: MIT
"""
from math import hypot

"""
python的内置类型, 如list/str/bytearray 等 CPython会抄近路, __len__ 实际上会直接返回
    PyVarObject里的ob_size属性

PyVarObject是表示内存中长度可变的内置对象的C语言结构体, 直接读取这个值比调用一个方法更快

很多时候, 特殊方法的调用是隐式的, 比如 for item in tasks: 这个语句背后其实用的是iter(tasks)
    而这个函数背后则是tasks.__iter__()方法, 当然, 前提是这个方法在tasks中被实现了
    
这里有一个例外: __init__方法需要在你的代码中经常用到它, 目的是在你的子类中的_init__方法调用超类中的构造器

PS: 不要自己想当然的刻意添加添加一些特殊方法 比如__foo__之类, 因为虽然这个名字暂时没有被Python内部使用, 以后就不一定了
"""


# 我们来实现一个二维向量(vector)类, 这个向量就是欧几里得几何中常用到的概念, 常在数学和物理中使用
# 一个Vector(2, 4) + Vector(2, 1) = Vector(4, 5)
# 这里将用到一些特殊方法的实现: __repr__, __abs__, __add__和 __mul__


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        """
        字符串表示形式:
            Python有一个内置的函数叫做repr, 他能把一个对象用字符串的形式表达出来以便辨认, 这就是字符串表示形式
            repr是通过__repr__这个特殊方法来得到一个对象的字符串表现形式, 如果没有实现__repr__ 当我们在控制台打印一个向量
            的实例的时候, 得到的是这个实例对象的内存地址 <__main__.Vector object at 0x10229b3c8>

            在选择__str__与__repr__时, 选择__repr__会更好, 如果一个对象没有__str__函数而Python有需要调用他时, 解释器会用
            __repr__作为替代

        ps: __repr__和__str__的区别在于, 后者是在str()函数被调用时使用, 或在print函数打印一个对象时调用
        """
        return f'Vector(x: {self.x}, y: {self.y})'
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        """
            尽管Python里有bool类型, 但实际上任何对象都可以用于布尔值的上下文,
            比如: if or while 或者 and or not运算符, 为了判断一个值x是为真还是为假 Python会调用bool(x)
            这个函数只会返回True or False
            
            默认情况下, 我们自定义的类实例对象始终被认为是真, 除非这个类对__bool__ 或者 __len__函数有自己的实现
            bool(x) 背后是调用 x.__bool__()的结果, 如果不存在__bool__方法, 那么 bool(x) 会尝试调用x.__len__()
            若返回0, 则bool会返回False, 否则返回True
            
            我们对__bool__的实现很简单, 如果一个向量的模是0, 则返回False, 其他情况则返回True, 因为__bool__函数返回
            类型应该是bool值, 所以我们通过bool(abs(self))把模值变成了bool值
            
            如果想让Vector.__bool__更高效, 可以采用这种方式实现
            
            def __bool__(self):
                return bool(self.x or self.y)
            
            他不那么易读, 但是可以从abs到__abs__到平方再到平方根这些中间步骤.
        :return:
        """
        return bool(abs(self))
    
    def __add__(self, other):
        """
            通过__add__实现Vector的+法运算
            被操作的两个向量: self和other 并没有被改变, 而是生成一个新的向量实例对象返回
            中缀运算符的基本原则就是不改变操作对象本身, 而生成一个新的值
        :param other: 一个Vector的实例对象
        :return: 一个新生成的Vector实例对象
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, other):
        """
            通过__mul__实现Vector的 * 法运算
        :param other: 一个Vector的实例对象
        :return: 一个新生成的Vector实例对象
        """
        return Vector(self.x * other, self.y * other)


if __name__ == '__main__':
    vector = Vector(3, 4)
    print(vector)
