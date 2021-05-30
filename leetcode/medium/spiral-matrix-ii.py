#https://leetcode.com/problems/spiral-matrix-ii/
class Solution:
    def generateMatrix(self, n: int):
        out = [[None for _ in range(n)] for _ in range(n)] 
        i , j = 0, 0
        way = (0,1)
        for k in range(n ** 2):
            out[i][j] = k + 1
            try:
                if out[i+way[0]][j+way[1]] is None:
                    i += way[0]
                    j += way[1]
                    continue
            except Exception:
                pass
            if way == (0, 1):
                way = (1, 0)
            elif way == (1, 0):
                way = (0, -1)
            elif way == (0, -1):
                way = (-1, 0)
            elif way == (-1, 0):
                way = (0, 1)
            i += way[0]
            j += way[1]
        return out
print(Solution().generateMatrix(3))