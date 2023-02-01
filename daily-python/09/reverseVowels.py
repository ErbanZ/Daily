'''
Date: 2022-09-21 20:59:45
LastEditors: r7000p
LastEditTime: 2022-09-21 21:08:25
FilePath: \Daily\daily-python\09\reverseVowels.py
'''
s = "leetcode"
vowels = "aeiouAEIOU"

def reverseVowels(s):
    i, j = 0, len(s)-1
    _s = list(s)
    while i < j:
        while _s[i] not in vowels and i < j:
            i += 1
        while _s[j] not in vowels and i < j:
            j -= 1
        _s[i], _s[j] = _s[j], _s[i]
        i += 1
        j -= 1
    return "".join(_s)

print(reverseVowels(s))