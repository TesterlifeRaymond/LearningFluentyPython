"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2017/11/28 下午3:21
@File: doctest.py
@License: MIT
"""

import collections
from random import choice, shuffle

Card = collections.namedtuple('Card', ['rank', 'suit'])

"""
>>> diamonds_a = Card('A', 'diamonds')
>>> print(diamonds_a.rank)
>>> print(diamonds_a.suit)

Python中存储系列数据，比较常见的数据类型有list，除此之外，还有tuple数据类型。相比与list，tuple中的元素不可修改，
在映射中可以当键使用。tuple元组的item只能通过index访问.
collections模块的namedtuple子类不仅可以使用item的index访问item，还可以通过item的name进行访问。
可以将namedtuple理解为c中的struct结构，其首先将各个item命名，然后对每个item赋予数据。
"""


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))
    #   卡牌总数量
    print(deck.ranks)
    #   卡牌数值
    print(deck.suits)
    #   卡牌的花色
    print(choice(deck))
    #   随机从牌中取出一张, 返回一个Card类型的卡牌数值及花色
    print(deck[:3])
    # 对卡牌类实例对象切片, 操作对象为self._cards 列表

    for card in deck:
        print(card)
 
    #   实现__getitem__后, 卡牌为可迭代对象, 因为我们在getitem中操作对象为list
    #   当然也支持反向迭代

    for card in reversed(deck):
        print(card)

    """
    迭代通常是隐式的, 譬如一个集合类型没有实现__contains__方法
        那么in运算符就会按照顺序做一次迭代搜索

    如果是排序呢? 我们按照规则用点数来判断大小, 2最小 A最大, 同事还要加上花色判定, 黑桃最大, 红桃次之,方片再次
        梅花最小......
    """
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


    def spades_high(cards):
        rand_value = FrenchDeck.ranks.index(cards.rank)
        return rand_value * len(suit_values) + suit_values[cards.suit]

    for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
        print(card)
        
    
#   Question?
"""
当前的设计是不可洗牌的, 因为这摞牌是不可变的 immutable类型
shuffle(deck._cards)
print(deck._cards)

或按照书中提到的__setitem__
"""
