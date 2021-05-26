#https://leetcode.com/problems/divide-two-integers/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        if dividend > 0 and divisor > 0:
            while dividend >= divisor:
                dividend -= divisor
                count += 1
        elif dividend < 0 and divisor < 0:
            while dividend <= divisor:
                dividend -= divisor
                count += 1
        elif dividend > 0 and divisor < 0:
            while dividend + divisor >= 0:
                dividend += divisor
                count -= 1
        elif dividend < 0 and divisor > 0:
            while dividend + divisor <= 0:
                dividend += divisor
                count -= 1
        return count
print(Solution().divide(-1, 1))