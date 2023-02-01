'''
Date: 2022-09-17 17:46:05
LastEditors: r7000p
LastEditTime: 2022-09-21 21:21:14
FilePath: \Daily\daily-python\09\merge.py
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # 1)
        # temp = nums1.copy()
        # i, j = 0, 0
        # for idx in range(m+n):
        #     if i < m and j < n:
        #         if temp[i] <= nums2[j]:
        #             nums1[idx] = temp[i]
        #             i += 1
        #         else:
        #             nums1[idx] = nums2[j]
        #             j += 1
        #     elif i < m and j >= n:
        #         nums1[idx] = temp[i]
        #         i += 1
        #     elif i >= m and j < n:
        #         nums1[idx] = nums2[j]
        #         j += 1

        # 2)
        i, j = m-1, n-1
        idx = m + n
        while idx > -1:
            idx -= 1
            if i > -1 and j > -1:
                if nums1[i] >= nums2[j]:
                    nums1[idx] = nums1[i]
                    i -= 1
                else:
                    nums1[idx] = nums2[j]
                    j -= 1
            elif i > -1:
                nums1[idx] = nums1[i]
                i -= 1
            elif j > -1:
                nums1[idx] = nums2[j]
                j -= 1

nums1 = [1]
nums2 = [0]
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
slt = Solution()
slt.merge(nums1, 3, nums2, 3)
print(nums1)
