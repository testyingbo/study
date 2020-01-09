#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
con =threading.Condition()
num = 0


# 生产者
class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global num
        # 锁定线程
        con.acquire()
        while True:
            print '开始添加！！'
            num = num + 1
            print '火锅里面鱼丸个数%s' %str(num)
            time.sleep(1)
            if num >= 5:
                print '火锅鱼丸5个了！！不能添加了！'
                # 唤醒等待的线程
                con.notify()  # 唤醒小伙伴开吃啦
                # 等待通知
                con.wait()
        con.release()


# 消费者
class Consumers(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # 锁定线程
        con.acquire()
        global num
        f = True
        while f:
            print '开吃！！'
            num = num - 1
            print '鱼丸剩余数量%s'%str(num)
            time.sleep(2)
            if num <= 0:
                f = False
                print '锅里没鱼丸了，赶紧添加！'
                # 唤醒等待的线程
                con.notify()  # 唤醒小伙伴开吃啦
        # 释放锁
        con.release()


p = Producer()
c = Consumers()
p.start()
c.start()
