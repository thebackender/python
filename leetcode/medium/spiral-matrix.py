#https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix):
        d = 0
        imax = len(matrix[0]) - 1 
        jmax = len(matrix) - 1
        imin, jmin = 0, 0
        data = []
        while imax >= imin and jmin <= jmax:
            if d == 0:
                for i in range(imin, imax + 1):
                    data.append(matrix[jmin][i])
                jmin += 1
            if d == 1:
                for j in range(jmin, jmax + 1):
                    data.append(matrix[j][imax])
                imax -= 1
            if d == 2:
                for i in range(imax, imin -1, -1):
                    data.append(matrix[jmax][i])
                jmax -= 1
            if d == 3:
                for j in range(jmax, jmin - 1, -1):
                    data.append(matrix[j][imin])
                imin += 1
            d += 1
            d %= 4
        return data
print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))