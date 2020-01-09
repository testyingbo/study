#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 假设你有无限数量的邮票,面值分别为6角，7角，8角,请问你最大的不可支付邮资是多少元
a = 6
b = 7
c = 8
t = 50
s = []
l = []
r = []
for i in range(t+1):
    s1 = i * a
    s.append(s1)
    for j in range(t+1):
        s2 = i*a + j*b
        s.append(s2)
        for k in range(t+1):
            s3 = i*a + j*b + k*c
            s.append(s3)
s.sort()
for n in s:
    if n in l:
        pass
    else:
        l.append(n)
for m in range(6*t):
    if m in l:
        pass
    else:
        r.append(m)
print r[-1]