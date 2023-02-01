'''
Date: 2022-10-30 18:55:31
LastEditors: r7000p
LastEditTime: 2022-10-30 19:45:52
FilePath: \Daily\daily-python\10\lengthOfLongestSubstring.py
'''

def lengthOfLongestSubstring(s):
    hashset = []
    res = 0
    for i in s:
        if i in hashset:
            res = max(res, len(hashset))
            hashset = hashset[hashset.index(i)+1:]
        hashset += [i]
    res = max(res, len(hashset))
    return res

s = "dvdf"
s = "pwwkew"
s = "adcasdvcb"
print(lengthOfLongestSubstring(s))
