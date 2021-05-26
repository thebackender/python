#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        minus = False
        if x < 0:
            x = abs(x)
            minus = True
        while int(x%10) or int(x/10):
            a = a*10 + x%10
            x = int(x/10)
        if pow(-2, 31) < a and a < pow(2, 31) - 1:
            if minus:
                return a*-1
            else:
                return a
        else:
            return 0
c = Solution()
print(c.reverse(120))