'''
Date: 2022-08-21 17:48:38
LastEditors: r7000p
LastEditTime: 2022-08-21 18:36:45
FilePath: \Daily\daily-python\08\rob.py
'''
class Solution:
    def rob(self, nums):
    #     def robHelper(nums, i):
    #         if i < 0: return 0
    #         lastLast = robHelper(nums, i - 2)
    #         last = robHelper(nums, i - 1)
    #         return max(last, lastLast + nums[i])
    #     return robHelper(nums, len(nums) - 1)
        # # 1. dp[i] 表示 i+1 个房屋的盗窃最大值
        # # 2. dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # # 3. dp[-1], dp[-2] = 0, 0
        n = len(nums)
        dp = [0] * n
        if n == 1:
            dp[0] = nums[0]
        elif n > 1:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

nums = [10,1,3,100]
nums = [2,7,9,3,1]
# nums = [1,2,3,1]
# nums = [0]
slt = Solution()
print(slt.rob(nums))
