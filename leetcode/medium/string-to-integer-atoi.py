#https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == "":
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        num = 0
        for a in s:
            if a.isdigit():
                num = num*10 + int(a)
            else:
                break
        return sign*min(pow(2, 31), num) if sign == -1 else sign*min(pow(2, 31) - 1, num)
print(Solution().myAtoi("21474836460"))