#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
# 如果多个线程同时操作某个数据，会出现不可预料的结果。比如以下场景：当小伙伴a在往火锅里面添加鱼丸的时候，小伙伴b在同时吃掉鱼丸,
# 这很有可能导致刚下锅的鱼丸被夹出来了（没有熟），或者还没下锅，就去夹鱼丸（夹不到）
# 为了避免以上这种情况发生，就引入锁的概念，锁有两种状态：锁定和未锁定
#
# 2.每当一个线程a要访问共享数据时，必须先获得锁定；如果已经有别的线程b获得锁定了，那么就让线程a暂停，也就是同步阻塞；
# 等到线程b访问完毕，释放锁以后，再让线程a继续。
#
# 3.用threading.Lock()这个类里面的两个方法
#
# acquire() 锁住
# release() 释放锁


# 定义执行函数
def chihuoguo(people, do):
    print('%s 吃火锅的小伙伴-羊肉：%s' % (time.ctime(), people))
    time.sleep(1)
    for i in range(3):
        time.sleep(1)
        print('%s%s 正在%s鱼丸'% (time.ctime(), people, do))
    print('%s 吃火锅的小伙伴-鱼丸：%s' % (time.ctime(), people))


# 定义自己的thread，继承threading.Thread,重写__init__和run方法
class MyThread(threading.Thread):
    lock = threading.Lock()     # 线程锁

    def __init__(self, people, name, do):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people
        self.do = do

    def run(self):
        '''重写run方法'''
        print '开始线程' + self.threadName
        self.lock.acquire()
        chihuoguo(self.people, self.do)
        self.lock.release()
        print '结束线程' + self.threadName


# 设置线程组
threads = []

# 创建新线程
thread1 = MyThread('小明', 'Thread-1', '添加')
thread2 = MyThread('小张', 'Thread-2', '吃掉')

threads.append(thread1)
threads.append(thread2)

for i in threads:
    i.start()

for i in threads:
    i.join()

time.sleep(0.5)
print '退出主线程：吃火锅结束，结账走人'
