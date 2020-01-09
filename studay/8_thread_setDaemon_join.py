#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
# 主线程结束了，子线程必须也跟着结束
#
# 1.主线程中，创建了子线程thread1和thread2，并且在主线程中调用了thread.setDaemon(),这个的意思是，把主线程设置为守护线程，这时候，要是主线程执行结束了，就不管子线程是否完成,一并和主线程退出.
# （敲黑板：必须在start()方法调用之前设置，如果不设置为守护线程，程序会被无限挂起。）
#
# 2.线程有一个布尔属性叫做daemon。表示线程是否是守护线程，默认取否。当程序中的线程全部是守护线程时，程序才会退出。只要还存在一个非守护线程，程序就不会退出。
# 主线程是非守护线程。
#
# 3.setDaemon(True)此方法里面参数设置为True才会生效
# 阻塞主进程join（timeout）
# 1.如果想让主线程等待子线程结束后再运行的话，就需要用到join(),此方法是在start之后（与setDaemon相反）
#
# 2.join(timeout)此方法有个timeout参数，是线程超时时间设置

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

# 守护线程setDaemon(True)
thread1.setDaemon(True)       # 必须在start之前
thread2.setDaemon(True)


thread1.start()
thread2.start()

# 阻塞主线程，等子线程结束,在start之后
# thread1.join()
# thread2.join()

time.sleep(0.5)
print '退出主线程'
