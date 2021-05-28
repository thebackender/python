#https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return float("{:.5f}".format(pow(x, n), 5))
print(Solution().myPow(2.00000, -2))