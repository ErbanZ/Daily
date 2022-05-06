# tab = ["chengdu", "ruanjianyuan", "xgimi"]
# text = "i live in chengdu."
# for val in tab:
#     if val in text:
#         print("string contain", val)

# if any(element in text for element in tab):
#     print("string contain chengdu")

from turtle import left


s0 = "a"
s1 = "babad"
s2 = "cbbd"
s3 = "aba"
s4 = "abba"
s5 = "aa"
s6 = "abcba"

def isPalindromic(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def LPS(s):
    if len(s) == 1:
        return s
    left, right = 0, 0
    for i in range(1, len(s)):
        # 奇回文
        curL, curR = i, i
        while curL >= 0 and curR < len(s):
            if s[curL] != s[curR]:
                break
            curL -= 1
            curR += 1
        if curR - curL - 2 > right - left:
            left = curL + 1
            right = curR - 1

        # 偶回文
        curL, curR = i, i - 1
        while curL >= 0 and curR < len(s):
            if s[curL] != s[curR]:
                break
            curL -= 1
            curR += 1
        if curR - curL - 2 > right - left:
            left = curL + 1
            right = curR - 1

    return s[left: right+1]

print(LPS(s0))
print(LPS(s1))
print(LPS(s2))
print(LPS(s3))
print(LPS(s4))
print(LPS(s5))
print(LPS(s6))
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
# https://rc.guizhou.gov.cn/
