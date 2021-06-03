#https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        i = 0
        for i, t in enumerate(matrix):
            if target >= min(t) and target <= max(t):
                break
        if target in matrix[i]:
            return True
        else:
            return False
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))