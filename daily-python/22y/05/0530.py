'''
Date: 2022-05-30 20:11:59
LastEditors: r7000p
LastEditTime: 2022-05-30 20:36:36
FilePath: \Daily\daily-python\05\0530.py
'''
# removeDuplicates
# removeDuplicates
# removeDuplicates

def removeDuplicates(nums):
    slow, fast = 0, 0
    n = len(nums)
    while slow < n and fast < n:
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1


nums1 = [0,0,1,1,1,2,2,3,3,4]
nums2 = [1]
nums3 = [1,1]
nums4 = [1,2]
nums5 = [1,1,2]
nums6 = [1,2,2]


print(removeDuplicates(nums1))
print(removeDuplicates(nums2))
print(removeDuplicates(nums3))
print(removeDuplicates(nums4))
print(removeDuplicates(nums5))
print(removeDuplicates(nums6))