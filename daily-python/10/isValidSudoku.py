'''
Date: 2022-10-24 21:26:00
LastEditors: r7000p
LastEditTime: 2022-10-24 22:01:21
FilePath: \Daily\daily-python\10\isValidSudoku.py
'''

def isValidSudoku(board):
    hashmapRow = dict()
    hashmapCol = dict()
    hashmapSqu = dict()
    m, n = len(board), len(board[0])
    for i in range(m):
        hashmapRow[i] = []
        for j in range(n):
            squNum = i // 3 * 3 + j // 3
            if i == 0:
                hashmapCol[j] = []
            if squNum not in hashmapSqu:
                hashmapSqu[squNum] = []
            if board[i][j].isdigit():
                # Row
                if board[i][j] in hashmapRow[i]:
                    return False
                hashmapRow[i] += [board[i][j]]
                # Column
                if board[i][j] in hashmapCol[j]:
                    return False
                hashmapCol[j] += [board[i][j]]
                # Square
                if board[i][j] in hashmapSqu[squNum]:
                    return False
                hashmapSqu[squNum] += [board[i][j]]
    return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
