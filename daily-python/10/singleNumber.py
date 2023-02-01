'''
Date: 2022-10-09 20:56:03
LastEditors: r7000p
LastEditTime: 2022-10-09 21:01:03
FilePath: \Daily\daily-python\10\singleNumber.py
'''

def singleNumber(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            hashset.remove(i)
        else:
            hashset.add(i)
    return hashset.pop()

nums = [1,2,3,3,2,1,4]
print(singleNumber(nums))