

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


strs0 = [""]
strs1 = ["flower"]
strs2 = ["flower", ""]
strs = ["flower","flow","flight"]
test = ["cir","car"]

def longestcommonprefix(strs):
    str = ""
    num = len(strs)
    if num == 1:
        str = strs[0]
        return str
    str = strs[0]
    for i in range(num):
        strtemp = str
        str = ""
        strnum = len(strtemp) if len(strs[i]) > len(strtemp) else len(strs[i])
        for j in range(strnum):
            if strtemp[j] == strs[i][j]:
                str += strtemp[j]
            else:
                break

    return str

# print(longestcommonprefix(strs0))
# print(longestcommonprefix(strs1))
# print(longestcommonprefix(strs))
# print(longestcommonprefix(test))

print(list(zip(*strs)))
print(list(zip(*zip(strs[0], strs[1], strs[2]))))
