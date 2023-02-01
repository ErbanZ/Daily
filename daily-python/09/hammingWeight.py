'''
Date: 2022-09-01 19:29:14
LastEditors: r7000p
LastEditTime: 2022-09-01 19:55:19
FilePath: \Daily\daily-python\09\hammingWeight.py
'''

class Solution:
    def hammingWeight(self, n):
        # # 1
        # return str(bin(n)).count('1')
        # 2
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count

n = 0b00000000000000000000000000001011
slt = Solution()
print(slt.hammingWeight(n))