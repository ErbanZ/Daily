'''
Date: 2022-08-28 20:21:13
LastEditors: r7000p
LastEditTime: 2022-08-28 22:03:36
FilePath: \Daily\daily-python\08\mergeSort.py
'''
import random

def mergeSort(nums):
    if len(nums) < 2: return nums
    # temp = []
    mid = len(nums) >> 1
    left, right = nums[:mid], nums[mid:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

def aNums(n):
    nums = []
    for i in range(n):
        nums.append(i)
    for i in range(n >> 1):
        l, r = random.randint(0, n-1), random.randint(0, n-1)
        nums[l], nums[r] = nums[r], nums[l]
    return nums

nums = aNums(20)
print(mergeSort(nums))
# print(nums)
