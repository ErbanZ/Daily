'''
Date: 2022-08-27 20:38:30
LastEditors: r7000p
LastEditTime: 2022-08-28 20:20:39
FilePath: \Daily\daily-python\08\generate.py
'''

# 杨辉三角
class Solution:
    def generate(self, numRows):
        rows = []
        if numRows == 1:
            rows = [[1]]
        elif numRows == 2:
            rows = [[1], [1, 1]]
        else:
            rows = [[1], [1, 1]]
            for i in range(2, numRows):
                row = []
                for j in range(i):
                    if j == 0:
                        row.append(1)
                    else:
                        row.append(rows[i-1][j-1] + rows[i-1][j])
                row.append(1)
                rows.append(row)
        return rows


# 1
# 11
# 121
# 1331

numRows = 5
slt = Solution()
print(slt.generate(numRows))