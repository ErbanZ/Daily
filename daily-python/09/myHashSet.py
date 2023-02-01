'''
Date: 2022-09-25 19:12:46
LastEditors: r7000p
LastEditTime: 2022-09-25 21:42:42
FilePath: \Daily\daily-python\09\myHashSet.py
'''

class MyHashSet:

    def __init__(self):
        self.hashset = set()

    def add(self, key):
        self.hashset.add(key)

    def remove(self, key):
        if self.contains(key):
            self.hashset.remove(key)

    def contains(self, key):
        return key in self.hashset

[].remove