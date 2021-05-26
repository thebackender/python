#https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        count = 0
        for i in range(1, n + 1):
            if i%5 == 0:
                while i%5 == 0:
                    count += 1
                    i //=5
        return count
print(Solution().trailingZeroes(80))