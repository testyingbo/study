#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
# os.popen() 方法返回一个file对象，可以使用open方法查看
# a = os.popen(r'python C:\Users\yingbojia\PycharmProjects\study\studay\13_yaml-study.py', 'r')    # popen 获取控制台输出方法
# d = a.read()
# print d
# a.close()
f = os.popen(r'adb devices', 'r')
shuchu = f.read()
f.close()
s = shuchu.split('\n')
new = [x for x in s if x != '']
devices = []
for i in new:
    dev = i.split('\tdevice')
    if len(dev) > 1:
        devices.append(dev[0])
    else:
        pass
if len(devices) == 0:
    print '没有手机连接'
else:
    print '有%s个手机连接'%str(len(devices))
    print '分别是：'
    for i in devices:
        print i