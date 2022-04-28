from traceback import print_tb


matrix0 = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]

matrix1 = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

def setZero(matrix):
    zeros = []
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zeros.append((i, j))
    for zero in zeros:
        for i in range(n):
            if matrix[i][zero[1]] != 0:
                matrix[i][zero[1]] = 0
        for j in range(m):
            if matrix[zero[0]][j] != 0:
                matrix[zero[0]][j] = 0

    

    # return matrix

setZero(matrix0)
setZero(matrix1)