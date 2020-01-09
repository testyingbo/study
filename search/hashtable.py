#!/usr/bin/python
# -*- coding: UTF-8 -*-
# hash查找


class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size  # 创建一个空槽列表，用来存储key，类似字典中的key
        self.data = [None] * self.size  # 创建一个空槽列表，用来存储data，类似字典中的value

    def hashfunction(self, key, size):  # 返回一个初始的哈希值
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def put(self, key, data):  # 添加新的值
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextsolt = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextsolt] != None and self.slots[nextsolt] != key:
                    nextsolt = self.rehash(nextsolt, len(self.slots))

                if self.slots[nextsolt] == None:
                    self.slots[nextsolt] = key
                    self.data[nextsolt] = data
                else:
                    self.data[nextsolt] = data

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        found = False
        stop = False
        position = startslot
        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                data = self.data[position]
                found = True

            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


H = HashTable()
H[54] = 'cat'
H[26] = 'dog'
H[93] = 'lion'
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print H.slots
print H.data
print H[20]
H[20] = 'duck'
print H[20]
print H[99]
H.put(66, 'test')
H.put(100, 'test2')
# H.put(90, 'test3')

print H.data