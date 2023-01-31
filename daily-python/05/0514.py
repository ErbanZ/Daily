# KMP

def getnext(s):
    next = [0] * len(s)
    i, j = 0, -1
    next[0] = -1
    while i < len(s) - 1:
        if j < 0 or s[i] == s[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]

    return next

def KMP(s, t):
    tn = getnext(t)
    i ,j = 0, 0
    while i < len(s) and j < len(t):
        if j < 0 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = tn[j]
    if j == len(t):
        print("current index: ", i - j)
        return True
    return False

if __name__ == "__main__":
    s = "ababababca"
    t1 = "abababca"
    t2 = "bababca"
    # s = "aaaaa"
    # t = "bba"
    print(KMP(s, t1))
    print(KMP(s, t2))
