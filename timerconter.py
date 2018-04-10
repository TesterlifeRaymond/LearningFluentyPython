
"""
#--coding:utf-8--
# Pw @2018-01-26 21:28:19
# Author: Ray
"""
from time import perf_counter
from collections import deque


def test_perf_counter():
    """
        python中高性能的计数器: perf_counter
    return: None
    """
    start = perf_counter()
    num = 0
    while num < 10:
        num += 1

    print(perf_counter() - start)


def test_deque():
    """
        collections.deque 是python中的双向队列
    """
    dq = deque(range(10), maxlen=10)
    # maxlen是可选参数, 代表这个队列最大可容纳元素的数量, 一旦设定, 这个队列的最大数量就不可以修改
    print(dq)
    dq.rotate(3)
    # 队列旋转操作接受一个参数n, 当n>0的时候, 队列最右边的n个元素被移动到队列的左边, 当n<0的时候,最左边的n个元素被移动到最右边
    print(dq)
    dq.rotate(-4)
    print(dq)

    dq.appendleft(-1)
    print(dq)
    # 当试图对一个d.maxlen已满的双向队列做尾部添加操作的时候, 他的头部元素会被删除掉

    dq.extend([11, 22, 33])
    print(dq)
    # 在尾部添加三个元素的操作会挤掉-1, ,1, 2

    dq.extendleft([10, 20, 30, 40])
    print(dq)
    # extendleft(iter)方法会把迭代器中的参数放入队列的左侧, 因此迭代器中的元素会逆序出现在队列中


# 双向队列实现了大部分列表所拥有的方法, 也有一些额外的符合自身设计的方法, 比如popleft, rotate
# 但是为了实现这些方法, 双向队列也付出了一些代价, 从队列中间删除元素的操作会慢一些, 因为他只对
# 头尾的操作进行了优化

# append 和 popleft 都是原子操作, 也就是deque可以在多线程程序中安全的当做先进先出的栈使用, 而使用者
# 不需要担心资源链的问题


"""
列表和双向的方法(不包括由对象实现的方法)

s.__add__(s2) : s + s2 拼接
s.__iadd__(s2) : s += s2 就地加法
s.append(s2) : 添加一个元素到最右侧(index, -1)
s.appendleft(s2): 添加一个元素到最左侧(index, 0)
...
"""


"""
除了deque, python标准库还提供了队列实现 Queue

提供了同步类(线程安全)Queue, LifoQueue, PriorityQueue, 不同线程可以利用这些数据类型交换信息
这三个类的构造方法都有一个可选参数maxsize, 他接受正整数作为输入值, 用来限定队列的大小, 但是在满员
的时候, 这些类不会扔掉旧的元素来腾位置, 相反他如果满了, 会被锁住, 直到领导的线程移除元素腾出位置
这一特性, 让这些类很适合控制活跃的线程数量
"""

"""
multiprocessing
    这个包实现了自己的Queue, 他跟queue.Queue类似, 是设计给进程间通信用的, 同时还提供了一个专门的
    multiprocessing.JoinableQueue类型, 可以让任务管理变得更安全
"""

"""
heapq
    跟上面三个模块不同的是, heapq没有队列类, 而是提供了heapqpush和heappop , 让用户可以把可变序列当做堆队列或者优先队列来使用
    到了这里, 我们对列表之外的类的介绍也就告一段落了, 是时候阶段性总结一下队列序列的探索, 注意, 我们还没有提到str和二进制序列
"""

# 要想写出优雅,高效地道的python代码, 对标准库的掌握是不可或缺的

# python中常见的序列类型: 可变类型/ 不可变类型
# 但是另外一种分类方式也很有用, 那就是把他们分为扁平序列和容器序列

# 扁平序列: 体积更小, 速度更快, 用起来更简单, 但是他z还能保存一些原子性的数据, 比如: 数字/字符/字节# 容器序列: 则比较灵活, 但当容器序列遇到可变对象时,用户就需要格外小心了, 因为这种组合时常搞出一些"意外", 特别是带嵌套的数据结构出现时, 用户要多花费一些心思来保证代码的正确


# 列表推导式/生成器表达式, 提供了灵活的构建和序列化序列的方式, 这两个工具都异常强大, 如果你不能熟悉的使用它们, 可以专门花时间练习一下, 它们其实不难, 而且用起来让人上瘾

# 元祖在python里扮演了两个角色, 他既可以用作无名称的字段和记录, 又可以看做不可变的列表, 当元组被当做记录来用的时候, 拆包是最安全可靠的从元组里提取不同字段信息的方式, 新引入的* 句法让元祖拆包的便利性更上一层楼, 让用户可以选择性忽略一些不需要的字段, 具名元祖也已经不是新的概念了, 但他似乎没有的重视, 就像普通元祖一样, 具名元祖的实例也很节省空间, 但他同时提供了方便的通过名字来获取元祖各字段信息的方式, 另外还有实用的._asdct()方法来把记录变成OrderedDict类型


# python中的二分查找算法实现
# bisect.insort

import bisect


def binary_search(lst, value):
    """
        基于bisect.bisect_left实现的二分查算法
    @param: lst -> 一个有序列表
    @type: lst -> list()
    @value: 需要在有序列表中查找的元素
    """
    item = bisect.bisect_left(lst, value)
    if item != len(lst) and lst[item] == value:
        return item
    raise ValueError


if __name__ == '__main__':
    lst = list(range(1000000))
    print(binary_search(lst, 532))

