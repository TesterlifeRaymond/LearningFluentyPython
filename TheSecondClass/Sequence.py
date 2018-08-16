"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2017/12/4 下午3:45
@File: Sequence.py
@License: MIT
"""

"""
# 2.2.1
Python从ABC哪里继承了统一的风格, 去处理序列数据这一特点, 不管是哪种数据结构, 字符串/列表/字节序列/数组/xml元素
    抑或是数据库查询结果,他们都共用一套丰富的操作: 迭代, 切片, 排序还有拼接
    
深入理解Python中的不同序列类型, 不但能让我们避免重新发明轮子, 他们的API还能帮助我们把自定义的API设计的跟原生序列一样
    或者是跟未来可能出现的序列类型保持兼容


Python标准库用C实现了丰富的序列类型 列举如下:

    容器序列:
        list, tuple, collections.deque 这些序列能存放不同的数据类型
    
    扁平序列:
        str, bytes, bytearray, memoryview, array.array 这些序列只能容纳一种类型

容器序列存放的是他们所包含的任意类型的对象的引用, 而扁平序列里存放的是值而不是引用, 换句话说, 扁平序列其实是一段内存空间
    由此可见扁平序列其实更加紧凑, 但是他里面只能存放诸如字符,字节,数值这样的基础类型


序列类型还能按照能否被修改来分类

    可变序列(MutableSequence):
        lsit, bytearray, array.array, collections.deque和memoryview
    
    不可变序列(Sequence):
        tuple, str, bytes
"""

"""
# 2.2.2
    列表推导式与可读性
    示例2-1 把一个字符串变成unicode码位列表
    
    列表推导式不会有变量泄漏的问题
    map配合filter的效率不一定会高于列表推导式
"""

symbols = '$)(!@#!#$'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

print([ord(symbol) for symbol in symbols])

x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

"""
# 2.2.3 笛卡尔积

    如前所述, 用列表推到可以生成两个或以上的可迭代类型的笛卡尔积, 笛卡尔积是一个列表
        列表中的元素是由输入的可迭代类型的元素对构成的元祖, 因此笛卡尔积列表的长度等于数据变量的长度的乘积
    
    列表推导的作用只有一个: 生成列表, 如果想生成其他类型的序列, 则看下一章, 生成器表达式
        
    如果你需要一个列表, 列表中有3个不同尺寸的T恤衫, 每个尺寸都有黑白2个颜色, 用列表推导式算出这个列表
    实例2-4 使用推导式计算笛卡尔积
"""

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

"""
# 2.2.4 生成器表达式
    
    虽然也可以用列表推导来初始化元祖, 数组或其他序列类型, 但是生成器表达式是更好的选择, 这是因为
        生成器表达式背后遵守了迭代器协议, 可以逐个的产出元素, 而不是先建立一个完整的列表, 然后再把这个列表传递到某个
        构造函数里面, 显然生成器表达式更节省内存
"""

x = 'ABC'
dummy = (ord(x) for x in x)
print(x)
print(dummy)

import array

print(array.array('I', (ord(x) for x in x)))

"""
# 2.3.1 元祖和记录
    
    元祖其实是对数据的记录: 元祖中的每个元素都存放了记录中的一个字段的数据, 外加这个字段的位置, 正式这个位置信息给数据赋予了意义
    
    在元祖数据中有一种常用的方法, 叫做元祖拆包或可迭代对象向拆包
"""

number = (1, 2, 3)
a, b, c = number
print(a, b, c)

# 还可以用运算符把一个可迭代对象拆开作为函数的参数

print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
# 可以用*运算符把一个可迭代的对象拆开作为函数的参数

# 这里元祖拆包的法则是让一个函数可以用元祖的形式返回多个值, 然后调用函数的代码就能轻松的返回这些值
# 比如: os.path.split() 函数就会返回路径的最后一个文件名组成的元祖(path, last_part)
# 在元祖拆包中, 我们并不是对所有的数据都感兴趣, _占位符能帮助处理这种情况, 下面这段代码也展示了他的用法
import os

_, filename = os.path.split('/Users/TheSecondClass/Sequence.py')
print(filename)

# 如果是做国际化软件, 那么_可能不是一个理想的占位符, 因为他是gettext.gettext函数的常用别名
# gettext模块的文档: https://docs.python.org/3/library/gettext.html 提到这一点

# 除此之外, 在元祖的拆包中使用* 也可以帮助我们把注意力集中在元祖的部分元素上. 用*来代表处理省下的元素
# 在Python中 函数用*args来获取不确定参数算是一种经典的写法, 于是Python3中这个概念扩展到了平行赋值

a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

"""
# 2.3.3 嵌套元祖拆包
    
    接收表达式的元祖可以是嵌套式的, 例如(a, b, (c, d)), 只要这个接受元祖的嵌套结构符合表达式本身的嵌套结构
        Python就可以做出正确的应对, 示例如下:
"""

metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)), ]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

"""
# 2.3.4 具名元祖

    collections.namedtuple 是一个工厂函数, 它可以用来构建一个带字段名的元祖和一个有名字的类
    
    用namedtuple构建的类的实例所消耗的内存和元祖是一样的, 因为字段名都被存在对应的类里面, 这个实例跟
        普通的对象比起来也要小一些, 因为Python不会用__dict__来存放这些实例的属性
    
    创建一个具名元祖需要两个参数, 一个是类名, 另一个是类的各个字段的名字, 后者可以是由数个字符串组成的可迭代
        对象, 或者是由空格分隔开的字段名组成的字符串, 除了从普通元祖哪里继承来的属性之外, 景园组还有一些自己
        专有的属性, 实例2-10中展示了几个最有用的:_fields雷属性, 类方法_make(iterable) 和实例方法 _asdict()
"""

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.country)
print(tokyo.population)
print(tokyo[0])

print(City._fields)


LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.2))
print(delhi_data)
delhi_data = City._make(delhi_data)
print(delhi_data)
print(delhi_data._asdict())

for key, value in delhi_data._asdict().items():
    print(key, ' ', value)


""" # 2.4 切片 """

"""
# 2.4.1 为什么切片和区间会忽略最后一个元素
    
    在切片和区间操作里不包含区分范围的最后一个元素是Python的风格, 这个习惯符合Python, C和其他语言以0位
        为其实下标的传统, 这样做带来的好处如下
        
    * 当只有最后一个位置信息时, 我们也可以快速的看出切片和区分里有几个元素, range(3)和my_list[:3]都返回3个元素
    
    * 当起止位置信息都可见时, 我们可以快速的计算出切片的区间和长度, 用后一个数减去第一个下标(stop - start)即可
    
    * 这样做也让我们可以利用任意一个下标来吧序列分割成不重叠的两部分, 只要写成my_list[:x] 和 my_list[x:]就可以
        了, 如下所示
"""

l = [10, 20, 30, 40, 50, 60]
print(l[:2])   # 在下标2的地方分割

print(l[2:])

print(l[:3])   # 在下标3的地方分割

print(l[3:])


"""
# 2.6 序列的增量赋值
"""


class Cards:
    def __init__(self, a):
        """
        :param a:
        """
        self.a = a
    
    def __iadd__(self, other):
        """
            如果实现了__iadd__方法 就会调用这个方法, 同时对可变序列例如(list, bytearray 和array.array)来说
            a会被就地改动, 就像调用a.extend(b) 一样, 但是如果a没有实现__iadd__的话, a += b的表达效果就变成了
            a = a + b一样, 首先计算a + b的值得到一个新的对象然后赋值给a, 也就是说这个表达式中, 变量名会不会被
            关联到新的对象, 完全取决于这个类型有没有实现__iadd__方法
        :param other:
        :return:
        """
        i = 0
        from itertools import zip_longest
        pairs = zip_longest(self.a, other.a, fillvalue=0)
        for p in pairs:
            self.a[i] = p[0] + p[1]
    
            i += 1
        return self.a


a = Cards([4, 5])
b = Cards([1, 2])
print(id(a))
a += b
print(id(a))
print(a)

# 准确来说, 可变序列一般都是先了__iadd__方法, 因此+= 是就地假发, 而不可变序列就不支持这个操作
# 对这个方法无从谈起

l = [1, 2, 3]
print(id(l))

l *= 2
print(l)
print(id(l))
