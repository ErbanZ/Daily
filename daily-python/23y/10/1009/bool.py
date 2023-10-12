'''
Description: Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加
Date: 2023-10-09 21:34:57
LastEditTime: 2023-10-11 20:21:00
FilePath: \daily-python\23y\10\1009\bool.py
'''


# print(True) # True
# print(False) # False

# print(type(True)) # bool
# print(type(False)) # bool

# print(True is 1) # False
# print(False is 0) # False
# print(True == 1) # True
# print(False == 0) # Ture

# print(True+False) # 1

# print(isinstance(True, int)) # True
# print(isinstance(False, int)) # True
# print(isinstance(True, bool)) # True
# print(isinstance(False, bool)) # True

# print(isinstance(bool(), int)) # True

empty_list = []
empty_set = set()
empty_tuple = ()
empty_dict = {}

fill_list = [1, 2,]
fill_set = {1, 2,}
fill_tuple = (1, 2,)
fill_dict = {"one":1, "two":2}

print(True if 0 else False) # False
print(True if "" else False) # False
print(True if empty_list else False) # False
print(True if empty_set else False) # False
print(True if empty_tuple else False) # False
print(True if empty_dict else False) # False

print(True if 1 else False) # True
print(True if "0" else False) # True
print(True if fill_list else False) # True
print(True if fill_set else False) # True
print(True if fill_tuple else False) # True
print(True if fill_dict else False) # True
