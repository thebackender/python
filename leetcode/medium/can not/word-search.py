#https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board, word: str) -> bool:
        def search(s, matrix):
            i, j = 0, 0
            for j, t in enumerate(matrix):
                if s >= min(t) and s <= max(t):
                    break
            for i, k in enumerate(matrix[j]):
                if s == k:
                    return [i, j]
            return -1
        def con(a, matrix, b):
            f = search(a, matrix)
            print(f)
            imax, jmax = len(matrix[0]), len(matrix)
            if f != -1:
                if f[0] < imax - 1:
                    if b == matrix[f[1]][f[0] + 1]:
                        return True
                if f[0] > 0:
                    if b == matrix[f[1]][f[0] - 1]:
                        return True
                if f[1] < jmax - 1:
                    if b == matrix[f[1] + 1][f[0]]:
                        return True
                if f[1] > 0:
                    if b == matrix[f[1] - 1][f[0]]:
                        return True
                return False
            else:
                return False
        for i in range(len(word)-1):
            if not con(word[i], board, word[i+1]):
                return False
        return True
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))