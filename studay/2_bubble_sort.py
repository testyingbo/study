#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 冒泡排序
l = [1, 6, 9, 4, 5, 7, 2, 8, 3]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
        else:
            pass
print l
