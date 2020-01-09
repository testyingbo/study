#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = ["b", "a", "c", "a", "c", "b", "d", "e", "c", "a", "c"]
duixiang = set(a)
d ={}
print d
for i in duixiang:
    d[i] = a.count(i)
print d.items()
a = sorted(d.items(), key=lambda x: x[1], reverse=True)
print a
