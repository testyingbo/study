#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time


# 定义执行函数
def chihuoguo(people):
    print('%s 吃火锅的小伙伴-羊肉：%s' % (time.ctime(), people))
    time.sleep(1)
    print('%s 吃火锅的小伙伴-鱼丸：%s' % (time.ctime(), people))


# 定义自己的thread，继承threading.Thread,重写__init__和run方法
class MyThread(threading.Thread):
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):
        '''重写run方法'''
        print '开始线程' + self.threadName
        chihuoguo(self.people)
        print '结束线程' + self.threadName


thread1 = MyThread('小明', 'Thread-1')
thread2 = MyThread('小张', 'Thread-2')

thread1.start()
thread2.start()

time.sleep(0.5)
print '退出主线程'
