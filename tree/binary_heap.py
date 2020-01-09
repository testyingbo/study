#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 二叉堆的实现


class BinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i / 2 > 0:
            if self.heaplist[i] < self.heaplist[i/2]:
                self.heaplist[i], self.heaplist[i/2] = self.heaplist[i/2], self.heaplist[i]
            i = i/2

    def insert(self, item):
        self.heaplist.append(item)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # 整理二叉树的排序属性，将小的节点作为根节点
    def perDpwn(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)    # 获取节点i的左右节点最小的一个（索引）
            if self.heaplist[i] > self.heaplist[mc]:   # 根节点和子节点的数据做比较，如果根节点大，则和最小的子节点数据交换
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    # 比较左子节点和右子节点中小的一个（索引）
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heaplist.pop()
        self.perDpwn(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist)/2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.perDpwn(i)
            i = i - 1


bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())