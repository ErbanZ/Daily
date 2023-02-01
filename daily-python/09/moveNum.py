'''
Date: 2022-09-08 09:08:50
LastEditors: r7000p
LastEditTime: 2022-09-08 17:41:43
FilePath: \Daily\daily-python\09\moveNum.py
'''

class Solution:
    def moveNum(self, nums, N):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j] != N:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1        
        print(nums, i)

nums = [0, 2, 3, 4, 1, 2, 3, 4, 0]

slt = Solution()
slt.moveNum(nums, 2)
