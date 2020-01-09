#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 检测字符串是否是对称字符串
from Deque import Deque


def palchecker(aString):
    charduque = Deque()

    for char in aString:
        charduque.addRear(char)

    stillEqual = True
    while charduque.size() > 1 and stillEqual:
        first = charduque.removeFront()
        last = charduque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


print palchecker('12321')