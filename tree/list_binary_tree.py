#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 列表实现二叉树


def binaryTree(r):
    return [r, [], []]


# 插入左子树
def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


# 插入右子树
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, value):
    root[0] = value


def getLeftChild(root):
    return root[1]


def getRirhtChild(root):
    return root[2]