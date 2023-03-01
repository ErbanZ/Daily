'''
Date: 2022-09-11 12:14:28
LastEditors: r7000p
LastEditTime: 2022-09-21 21:21:11
FilePath: \Daily\daily-python\09\removeDuplicates2.py
'''

class Solution:
    def removeDuplicates(self, nums, n):
        _nums = []
        numsSet = []
        for num in nums:
            if num not in numsSet:
                numsSet.append(num)
        for num in numsSet:
            n = nums.count(num)
            if n > 2:
                n = 2
            _nums.extend([num] * n)        
        nums[:] = _nums[:]
        return len(nums)

        i = 0
        for num in nums:
            if i < n or num != nums[i-n]:
                nums[i] = num
                i += 1
        return i

nums = [0,0,1,1,1,1,2,3,3]
nums = [1,1,1,2,2,3]
nums = [-1,0,0,0,0,3,3]
nums = [0,0,3,3]
slt = Solution()
print(slt.removeDuplicates(nums, 1))
print(nums)
