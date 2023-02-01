'''
Date: 2022-10-18 19:59:12
LastEditors: r7000p
LastEditTime: 2022-10-18 20:08:10
FilePath: \Daily\daily-python\10\intersect.py
'''

def intersect(nums1, nums2):
    hashmap = dict()
    res = []
    for i in nums1:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for i in nums2:
        if i in hashmap:
            res += [i]
            hashmap[i] -= 1
            if hashmap[i] == 0:
                hashmap.pop(i)
    return res

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))