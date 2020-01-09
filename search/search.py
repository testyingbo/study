#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 顺序查找


def sqeuentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def search(alist, item):
    found = False
    for i in alist:
        if i == item:
            found = True
            break
    return found


print sqeuentialSearch([45,65,42, 78,1,89,23], 3)
print search([45,65,42, 78,1,89,23], 3)