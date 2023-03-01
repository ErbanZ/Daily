'''
Date: 2022-09-15 08:38:56
LastEditors: r7000p
LastEditTime: 2022-09-15 18:19:23
FilePath: \Daily\daily-python\09\findKthLargest.py
'''

def quickSort(nums, reverse=False):
    quickSortHelper(nums, 0, len(nums), reverse)

def quickSortHelper(nums, left, right, reverse=False):
    if right <= left:
        return
    pivot = left
    tempidx = pivot + 1
    for i in range(tempidx, right):
        if reverse == False:
            if nums[i] < nums[pivot]:
                nums[i], nums[tempidx] = nums[tempidx], nums[i]
                tempidx += 1
        else:
            if nums[i] > nums[pivot]:
                nums[i], nums[tempidx] = nums[tempidx], nums[i]
                tempidx += 1
    tempidx -= 1
    nums[pivot], nums[tempidx] = nums[tempidx], nums[pivot]

    quickSortHelper(nums, left, tempidx, reverse)
    quickSortHelper(nums, tempidx+1, right, reverse)

# 1) 找到 pivot
# 2) 基于 pivot 进行排序
# 3) 将 pivot 置于正确的位置
# 4) 将 pivot 两侧的数组重复上诉步骤
# 5) left >= right 时返回

# nums = [4,6,8,1,5,7,3,9,2,0,3]
# quickSort(nums, True)
# print(nums)

class Solution:
    def findKthLargest(self, nums, k):
        quickSort(nums=nums, reverse=True)
        return nums[k-1]

k = 4
nums = [4,6,8,1,5,7,3,9,2,0,3]
slt = Solution()
print(slt.findKthLargest(nums, k))

