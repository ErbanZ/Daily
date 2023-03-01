'''
Date: 2022-10-17 21:12:53
LastEditors: r7000p
LastEditTime: 2022-10-17 21:19:59
FilePath: \Daily\daily-python\10\firstUniqChar.py
'''

def firstUniqChar(s: str) -> int:
    hashmap = dict()
    for i in s:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for i in hashmap:
        if hashmap[i] == 1:
            return s.find(i)
    return -1

s = "loveleetcode"
print(firstUniqChar(s))