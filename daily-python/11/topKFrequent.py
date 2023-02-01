'''
Date: 2022-11-01 19:44:46
LastEditors: r7000p
LastEditTime: 2022-11-01 21:17:46
FilePath: \Daily\daily-python\11\topKFrequent.py
'''

def topKFrequent(nums, k):
    hashmap = dict()
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    hashmap = sorted(hashmap.items(), key=lambda x : x[1], reverse=True)
    res = [hashmap[i][0] for i in range(k)]
    return res

nums = [1,1,1,3,2,2]
k = 2
print(topKFrequent(nums, k))