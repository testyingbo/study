#!/usr/bin/python
# -*- coding: UTF-8 -*-
from stack import Stack
# 十进制转化为其他2/8/16进制


def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber / base

    newString = ''

    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString


a = baseConverter(1899, 16)
print a