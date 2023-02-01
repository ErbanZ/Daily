'''
Date: 2022-07-03 15:08:10
LastEditors: r7000p
LastEditTime: 2022-07-03 15:24:57
FilePath: \Daily\daily-python\07\KthLargest.py
'''

class KthLargest:

    def __init__(self, k, nums):
        self.l = nums
        self.k = k

    def add(self, val: int) -> int:
        self.l.append(val)
        self.l.sort()
        return self.l[-self.k]


kth = KthLargest(3, [4, 5, 8, 2])
print(kth.add(3))
print(kth.add(5))
print(kth.add(10))
print(kth.add(9))
print(kth.add(4))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)