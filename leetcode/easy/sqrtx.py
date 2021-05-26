#https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(pow(x, 1/2))
print(Solution().mySqrt(123))