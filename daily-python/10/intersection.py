'''
Date: 2022-10-10 21:35:29
LastEditors: r7000p
LastEditTime: 2022-10-10 23:11:08
FilePath: \Daily\daily-python\10\intersection.py
'''

def intersection(nums1, nums2):
    hashset = set()
    for i in nums1:
        if i in nums2:
            hashset.add(i)
    return list(hashset)

nums1 = [4,9,5,8]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
