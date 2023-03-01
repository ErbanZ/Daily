'''
Date: 2022-09-06 10:31:39
LastEditors: r7000p
LastEditTime: 2022-09-06 12:14:51
FilePath: \Daily\daily-python\09\moveZeros.py
'''

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # i, j = 0, 0
        # n = len(nums)
        # while i < n and j < n:
        #     while i < n and nums[i] != 0:
        #         i += 1
        #     if i < n and i <= j and nums[i] == 0 and nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #     j += 1
        # print(nums)

        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        print(nums)

nums = [0]
nums = [1]
nums = [1,0]
nums = [0,1,0,3,12]
nums = [1,3,12]
slt = Solution()
slt.moveZeroes(nums)
