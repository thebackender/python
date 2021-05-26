#https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        i = 0
        for i, a in enumerate(columnTitle[::-1]):
            num += (ord(a) - 64)*(26**i)
        return num
print(Solution().titleToNumber('ZY'))