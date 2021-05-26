#https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2, n3 = 0, 1, 1
        for _ in range(n):
            n3 = n1+n2
            n1, n2 = n2, n3
        return n3
print(Solution().climbStairs(6))