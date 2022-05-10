# 字符串匹配算法：KMP
# https://leetcode-cn.com/leetbook/read/array-and-string/cpoo6/

s = "ababababca"
s1 = "aaaaaaaab"
t = "abababca"
t1 = "aaaaaab"


def simplematchstring(s1, s2):
    i = 0
    while i <= len(s1) - len(s2):
        idx = i
        n = len(s2)
        for j in s2:
            if s1[idx] != j:
                break
            n -= 1
            idx += 1
        if n == 0:
            return True
        i += 1
    return False

def getPMT(s):
    res = [0] * len(s)
    i, j = 1, 0
    while i < len(s):
        if s[i] == s[j]:
            res[i] = j + 1
            i += 1
            j += 1
        else:
            j = res[i]
            i += 1
    return res

def KMP(s, t):
    tn = getPMT(t)
    i, j = 0, 0
    while j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = tn[j-1]
    if j == len(t):
        return True
    return False        

if __name__ == "__main__":
    # print(simplematchstring(s, t))
    print(KMP(s, t))
    print(KMP(s1, t1))
