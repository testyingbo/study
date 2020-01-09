#!/usr/bin/python
# -*- coding: UTF-8 -*-


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]


# 冒泡排序
def bubblesort(list):
    for i in range(0, len(list)-1):  # 一共进行len(list)-1轮比较
        for j in range(0, len(list)-1-i):  # 每轮比较len(list)-1-i次
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list


# 短冒泡排序，在冒泡排序基础上增加判断，当列表已经排好许时，停止程序执行
def shortBubbleSort(list):
    exchanges = True
    passnum = len(list) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                exchanges = True
        passnum = passnum - 1
    return list


# print bubblesort(alist)
# print shortBubbleSort(alist)


# 选择排序法
def selectsort(list):
    length = len(list)
    for i in range(0, length - 1):
        for j in range(i, length):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
        print list
    return list


# print selectsort(alist)


# 插入排序法
def insertSort(list):
    for index in range(1, len(list)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1
        list[position] = currentvalue

    return list


# print insertSort(alist)


# 希尔排序
def shellSort(alist):
    sublistcount = len(alist)/2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print "After increments of size", sublistcount, "The list is", alist

        sublistcount = sublistcount / 2
    return alist


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position] = currentvalue


# print shellSort(alist)


# 归并排序
def mergeSort(alist):
    print ('Splitting:', alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    print ('Merging:', alist)


# mergeSort(alist)
# print alist


# 快速排序法
def quickSort(list):
    quickSorthepler(list, 0, len(list)-1)


def quickSorthepler(list, first, last):
    if first < last:
        splitpoint = partition(list, first, last)

        quickSorthepler(list, first, splitpoint-1)
        quickSorthepler(list, splitpoint+1, last)


def partition(list, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while pivotvalue >= list[leftmark] and leftmark <= rightmark:
            leftmark = leftmark + 1

        while pivotvalue <= list[rightmark] and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            list[leftmark], list[rightmark] = list[rightmark], list[leftmark]

    list[first], list[rightmark] = list[rightmark], list[first]
    return rightmark


quickSort(alist)
print alist