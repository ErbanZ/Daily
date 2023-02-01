'''
Date: 2022-09-13 19:16:07
LastEditors: r7000p
LastEditTime: 2022-09-21 21:16:45
FilePath: \Daily\daily-python\09\sortColors.py
'''

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 1
        # temp = [0, 0, 0]
        # for n in nums:
        #     if n == 0:
        #         temp[0] += 1
        #     elif n == 1:
        #         temp[1] += 1
        #     else:
        #         temp[2] += 1
        # nums.clear()
        # nums[:] = [0] * temp[0] + [1] * temp[1] + [2] * temp[2]

        # 2
        n = len(nums) - 1
        l, r = 0, n
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1

nums = [2,0,2,1,1,0]
nums = [1,0,2,2,1,0]
nums = [1,2,2,2,1,0]
nums = [2,0,1]

slt = Solution()
slt.sortColors(nums)
print(nums)