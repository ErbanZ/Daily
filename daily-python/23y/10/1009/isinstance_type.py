"""
type 主要用于判断未知数据类型
isinstance 主要用于判断 A 类是否继承于 B 类
"""

class A():
    pass

class B(A):
    pass

# 类
print(A)
print(B)

# 类实例
print(A())
print(B())

# 类的类型
print(type(A))
print(type(B))

# 类实例的类型
print(type(A()))
print(type(B()))

print(type(A()) == A) # True
print(type(A()) == B) # False
print(isinstance(B(), A)) # True
# print(isinstance(B(), A())) # TypeError: isinstance() arg 2 must be a type or tuple of types

print(type(True))
print(isinstance(True, int))