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

matrix6 = [
    [4,33,13,32,12,2],
    [24,1,7,33,27,29],
    [1,20,32,2,14,20],
    [6,28,32,27,25,26],
    [32,21,22,9,13,16],
    [34,7,26,14,21,28]
]

# m4 = [
#     [5,1,9,11],
#     [2,4,8,10],
#     [13,3,6,7],
#     [15,14,12,16]
# ]

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
    loops = n // 2
    for i in range(loops):
        for j in range(n - 1 - i*2):
            val = matrix[i+j][i]
            matrix[i+j][i] = matrix[n-i-1][i+j]
            matrix[n-i-1][i+j] = matrix[n-i-j-1][n-i-1]
            matrix[n-i-j-1][n-i-1] = matrix[i][n-i-j-1]
            matrix[i][n-i-j-1] = val

    return matrix

# print(rotate90(matrix3))
# print(rotate90(matrix4))
print(rotate90(matrix6))

# 未激活：
# SWJ2N1C81YWN（3709）
# SWQBM2646YWY（0315，未领取）
# SWQBM2721YWS（0315）
# SWJ2N1C33YWK（1890）
# SWQBM2664YWY
# SWJ2N1C45YWN（8865）
# SWQBM2784YW3（8865）
# SWQBM27FCYWJ

# 已激活，拉黑：
# SWQBM2712YWS（1152）
# SWJ2N1B1FYWU（8865，过期）
# SWJ2N1B76YWR（8865，过期）
# SWJ2N1B34YWK（8865）
# SWQBM2718YWY（8865）
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
# SWQBM2748YW3（0315）
# SWJ2N1B5EYWX（0315，实机）
# SWJ2N1AD7YWX（6369）
# SWQBM2667YW3（1615）
# SWQBM265EYW9（！！！）
# SWQBM2685YW3（2934）
# SWQBM274BYW6（5890）
# SWQBM279ZYW1（3709）

