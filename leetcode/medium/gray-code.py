#https://leetcode.com/problems/gray-code/
class Solution:
    def grayCode(self, n: int):
        return [i^i>>1 for i in range(2**n)]
print(Solution().grayCode(5))