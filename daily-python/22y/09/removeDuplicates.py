'''
Date: 2022-09-09 21:03:54
LastEditors: r7000p
LastEditTime: 2022-09-11 12:13:56
FilePath: \Daily\daily-python\09\removeDuplicates.py
'''

class Solution:
    def removeDuplicates(self, nums):
        # i = 0
        # for n in nums:
        #     if n > nums[i]:
        #         i += 1
        #         nums[i] = n
        # return i+1
        n = len(nums)
        j = 0
        for i in range(n):
            nums[i] = nums[j]
            j = i
            while j < n and nums[j] <= nums[i]:
                j += 1
            if j >= n: break
        return i+1
            
        
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]
slt = Solution()
print(slt.removeDuplicates(nums))
print(nums)