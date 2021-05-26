#https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        j = 1
        s = ""
        while columnNumber:
            k1 = columnNumber % (26**(j))
            if k1 == 0:
                s += 'Z'
                columnNumber -= (26**j)
            else:
                k2 = k1 // (26**(j-1))
                s += chr(64 + k2)
                columnNumber -= k2*(26**(j-1))
            j += 1
        return s[::-1]
print(Solution().convertToTitle(701))