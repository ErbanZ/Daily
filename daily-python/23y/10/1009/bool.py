'''
Description: Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加
Date: 2023-10-09 21:34:57
LastEditTime: 2023-10-09 22:04:53
FilePath: \daily-python\23y\10\1009\bool.py
'''


print(True) # True
print(False) # False

print(type(True)) # bool
print(type(False)) # bool

print(True is 1) # False
print(False is 0) # False
print(True == 1) # True
print(False == 0) # Ture

print(True+False) # 1

print(isinstance(True, int)) # True
print(isinstance(False, int)) # True
print(isinstance(True, bool)) # True
print(isinstance(False, bool)) # True

print(isinstance(bool(), int)) # True
