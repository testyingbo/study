#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 烫手的山芋游戏
from queue_study.Queue_study import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(["1", '2', "3", "4", "5", "6"], 1))