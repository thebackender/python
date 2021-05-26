#https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        d = {1000: 'M',100: 'C',10: 'X',1: 'I'}
        four = {'I': 'V','X': 'L','C': 'D'}
        nine = {'I': 'X','X': 'C','C': 'M'}
        five = {'I': 'V','X': 'L','C': 'D'}
        for k, v in d.items():
            r = num//k
            if r == 4:
                s += (v + four[v])
            elif r == 9:
                s += (v+nine[v])
            elif r >= 5:
                b = r%5
                s += (five[v] + v*b)
            else:
                s += v*r
            num %= k
        return s
print(Solution().intToRoman(1994))