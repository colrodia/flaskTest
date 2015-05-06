# -*- coding:utf-8 -*-
__author__ = 'jinjuoh'

class Calculator:
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def sum(self):
        return self._left + self._right


class User:
    def __init__(self, right):
        self._right = right

    def my(self):
        return self._right

c = Calculator(1,2)
print(c.sum())

u = User(10000)
print(u.my())