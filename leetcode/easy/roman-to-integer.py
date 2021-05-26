#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        arr = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        con = {
            'V': 'I',
            'X': 'I',
            'L': 'X',
            'C': 'X',
            'D': 'C',
            'M': 'C'
        }
        nex = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }
        ignore = False
        for i in range(len(s)):
            if ignore:
                ignore = False
                continue
            if i < len(s) - 1:
                if s[i] in nex and s[i+1] in nex[s[i]]:
                    num += arr[s[i+1]] - arr[con[s[i+1]]]
                    ignore = True
                else:
                    num += arr[s[i]]
            else:
                num += arr[s[i]]                
        return num
c = Solution()
print(c.romanToInt("MCMXCIV"))