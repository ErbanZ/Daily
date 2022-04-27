'''
Date: 2022-04-25 20:14:32
LastEditors: r7000p
LastEditTime: 2022-04-26 23:54:25
FilePath: \Daily\daily-python\april\0425.py
'''

from asyncore import loop


matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix4 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def rotate90(matrix):
    # n = len(matrix)
    # for i in range(n):
    #     for j in range(i):
    #         temp = matrix[i][j]
    #         matrix[i][j] = matrix[j][i]
    #         matrix[j][i] = temp
    
    # for i in range(n):
    #     for j in range(n // 2):
    #         temp = matrix[i][j]
    #         matrix[i][j] = matrix[i][n-j-1]
    #         matrix[i][n-j-1] = temp

    n = len(matrix)
    edgeLength = n - 1
    loops = n // 2
    for i in range(loops):
        for j in range(edgeLength):
            val = matrix[j+1][i]
            matrix[j+1][i] = matrix[n-i-1][j+1]
            matrix[n-i-1][j+1] = matrix[n-j-2][n-i-1]
            matrix[n-j-2][n-i-1] = matrix[i][n-j-2]
            matrix[i][n-j-2] = val

    return matrix

print(rotate90(matrix3))
print(rotate90(matrix4))


# 未激活：
# SWJ2N1C81YWN（3709）
# SWQBM2646YWY（0315，未领取）
# SWQBM2721YWS（安装）
# SWJ2N1C33YWK（1890）
# SWQBM2664YWY
# SWJ2N1C45YWN（8865）
# SWQBM2784YW3（8865）
# SWQBM27FCYWJ
# SWQBM279ZYW1
# SWJ2N1B73YWN
# SWQBM2685YW3
# SWQBM274BYW6
# GWL4M268ZYBP
# SWQBM2748YW3

# 已激活，拉黑：
# SWQBM2712YWS（1152）
# SWJ2N1B1FYWU（8865）
# SWJ2N1B76YWR（8865）
# SWJ2N1B34YWK
# SWQBM2718YWY
# SWJ2N1C4EYWX
# SWQBM2781YWY
# SWQBM2793YW3

# 已激活：
# SWJ2N1CCZYWS（0315，已领取）
# SWJ2N1CEDYW8（0315，已领取）
# SWJ2N1BAZYWP（2934）
# SWQBM26D6YW9（0315，已领取）
# SWJ2N1B22YWG（0315，已领取）
# SWJ2N1AFEYW8（0315，已领取）
# SWJ2N1AD7YWX（6369）
# SWQBM2667YW3（1615）
# SWQBM265EYW9（！！！）

