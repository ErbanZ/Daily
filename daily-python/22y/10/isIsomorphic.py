'''
Date: 2022-10-16 14:59:45
LastEditors: r7000p
LastEditTime: 2022-10-16 15:15:40
FilePath: \Daily\daily-python\10\isIsomorphic.py
'''

def isIsomorphic(s: str, t: str) -> bool:
    hashmap = dict()
    n = len(s)
    for i in range(n):
        if s[i] in hashmap and hashmap[s[i]] != t[i]:
            return False
        elif s[i] not in hashmap:
            if t[i] in hashmap.values():
                return False
            hashmap[s[i]] = t[i]
    return True

s = "foo"
t = "bar"
print(isIsomorphic(s, t))
