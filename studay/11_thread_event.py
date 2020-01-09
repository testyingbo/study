#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
from tomorrow import threads
event = threading.Event()



def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print '%s 已经启动' % threading.currentThread().getName()
    print '小伙伴%s已经进入就餐状态'%name
    time.sleep(1)
    event.wait()
    print '%s 收到通知了.' % threading.currentThread().getName()
    print '小伙伴 %s 开始吃咯！' % name


class MyThread(threading.Thread):
    def __init__(self, people):
        threading.Thread.__init__(self)
        self.people = people

    def run(self):
        chihuoguo(self.people)
        print("结束线程: %s" % threading.currentThread().getName())

# 设置线程组
threads = []

# 创建新线程
thread1 = MyThread('a')
thread2 = MyThread('b')
thread3 = MyThread('c')

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
for i in threads:
    i.start()

time.sleep(0.5)
# 发送事件通知
print '主线程通知小伙伴开吃咯！'
event.set()


