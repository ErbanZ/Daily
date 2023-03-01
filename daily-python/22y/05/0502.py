'''
Date: 2022-05-02 13:53:59
LastEditors: r7000p
LastEditTime: 2022-05-02 16:42:25
FilePath: \Daily\daily-python\05\0502.py
'''

from distutils.log import error


matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix4 = [
    [1,  2,  3],
    [5,  6,  7],
    [9, 10, 11],
    [13, 14, 15]
]

matrix6 = [
    [4,33,13,32,12,2],
    [24,1,7,33,27,29],
    [1,20,32,2,14,20],
    [6,28,32,27,25,26],
    [32,21,22,9,13,16],
    [34,7,26,14,21,28]
]


def diagonal(mat):
    res = []
    row, col = 0, 0
    n, m = len(mat), len(mat[0])
    for num in range(n+m-1):
        order = []
        tempR, tempC = row, col

        while 0 <= tempR < n and 0 <= tempC < m:
            order.append(mat[tempR][tempC])
            tempR += 1
            tempC -= 1

        if num % 2 == 0:
            res += reversed(order)
        else:
            res += order

        if col < m - 1:
            col += 1
        elif row < n - 1:
            row += 1

    return res

print(diagonal(matrix3))

# 0 (0,0) 
# 1 (0,1)(1,0)
# 2 (0,2)(1,1)(2,0)
# 3 (1,2)(2,1)
# 4 (2,2)

