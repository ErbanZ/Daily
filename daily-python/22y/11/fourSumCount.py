'''
Date: 2022-11-07 20:42:37
LastEditors: r7000p
LastEditTime: 2022-11-07 21:02:39
FilePath: \Daily\daily-python\11\fourSumCount.py
'''

# (a + b) = -(c + d)
def fourSumCount(nums1, nums2, nums3, nums4):
    hashmap = dict()
    res = 0
    for i in nums1:
        for j in nums2:
            n = i + j
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
    for i in nums3:
        for j in nums4:
            n = -(i + j)
            if n in hashmap:
                res += hashmap[n]
    return res

nums1 = [-1,-1]
nums2 = [-1,1]
nums3 = [-1,1]
nums4 = [1,-1]
print(fourSumCount(nums1, nums2, nums3, nums4))