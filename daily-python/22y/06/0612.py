'''
Date: 2022-06-12 13:44:30
LastEditors: r7000p
LastEditTime: 2022-06-12 14:57:05
FilePath: \Daily\daily-python\06\0612.py
'''


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for bracket in s:
            if bracket == '(':
                stack.append(')')
            elif bracket == '[':
                stack.append(']')
            elif bracket == '{':
                stack.append('}')
            elif not stack or bracket != stack.pop():
                return False

        return False if stack else True


s1 = r"){"
s2 = r"()[]{}"
s3 = r"(]"
s4 = r"([{}])"

slt = Solution()
print(slt.isValid(s1))
print(slt.isValid(s2))
print(slt.isValid(s3))
print(slt.isValid(s4))