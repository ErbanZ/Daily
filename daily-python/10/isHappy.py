'''
Date: 2022-10-11 22:05:56
LastEditors: r7000p
LastEditTime: 2022-10-11 22:29:02
FilePath: \Daily\daily-python\10\isHappy.py
'''

hashset = set()

def isHappy(n):
    sum = 0
    if n == 1:
        return True
    if n in hashset:
        return False
    else:
        hashset.add(n)
    for i in str(n):
        sum += int(i) * int(i)
    return isHappy(sum)

n = 10
print(isHappy(n))

