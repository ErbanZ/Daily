'''
Date: 2022-05-29 14:08:31
LastEditors: r7000p
LastEditTime: 2022-05-30 20:11:47
FilePath: \Daily\daily-python\05\0529.py
'''
# findMin
# findMin
# findMin
def findMin(nums):
    res = 0
    if len(nums) == 1: return nums[0]
    mid = len(nums) >> 1
    if nums[mid] > nums[0]:
        for i in range(len(nums)-1, -1, -1):
            if nums[i-1] > nums[i]:
                res = i
                break
    else:
        for i in range(len(nums)):
            if nums[i+1] < nums[i]:
                res = i + 1
                break
    return nums[res]

nums = [3,4,5,1,2]
# nums = [4,5,1,2,3]
# nums = [3,4,5,0,1,2]
# nums = [2, 1]
# nums = [1, 2]

# for i in range(len(nums)-1, -1, -1):
#     print(nums[i])

# print(findMin(nums))

