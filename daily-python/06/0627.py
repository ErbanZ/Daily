'''
Date: 2022-06-27 19:45:30
LastEditors: r7000p
LastEditTime: 2022-06-27 20:27:26
FilePath: \Daily\daily-python\06\0627.py
'''

class Solution:
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        resMat = [[0] * n for i in range(m)]
        roots = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        queue = []
        queue.extend(roots)
        visited = set(roots)

        while queue:
            _i, _j = queue.pop(0)
            for i, j in [(_i-1, _j), (_i+1, _j), (_i, _j-1), (_i, _j+1)]:
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                    resMat[i][j] = resMat[_i][_j] + 1
                    queue.append((i, j))
                    visited.add((i, j))

        return resMat

mat1 = [[0,0,0],[0,1,0],[0,0,0]]
mat2 = [[0,0,0],[0,1,0],[1,1,1]]

slt = Solution()
print(slt.updateMatrix(mat1))
print(slt.updateMatrix(mat2))
