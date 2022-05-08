# 字符串匹配算法：KMP
# https://leetcode-cn.com/leetbook/read/array-and-string/cpoo6/

s = "AAAAABBAAG"
t = "ABBACG"

def matchstring(s1, s2):
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
                
if __name__ == "__main__":
    print(matchstring(s, t))
