'''
Date: 2022-10-23 20:33:30
LastEditors: r7000p
LastEditTime: 2022-10-23 20:44:25
FilePath: \Daily\daily-python\10\groupAnagrams.py
'''

def groupAnagrams(strs):
    hashmap = dict()
    res = []
    for i in strs:
        s = ''.join(sorted(i))
        if s not in hashmap:
            hashmap[s] = [i]
        else:
            hashmap[s] += [i]
    for i in hashmap.values():
        res += [i]
    return res

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))