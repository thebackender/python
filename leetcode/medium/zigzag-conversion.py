#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zigzag = ""
        d = {}
        i, j = 0, 0
        mode = "down"
        while len(s):
            if j not in d:
                d[j] = s[0]
            else:
                d[j] += s[0]
            if j == numRows - 1:
                mode = "up"
            elif j == 0:
                mode = "down"
            if mode == "down":
                j += 1
            elif mode == "up":
                j -= 1
                i += 1
            s = s[1:]
        for k, v in d.items():
            zigzag += v
        return zigzag
print(Solution().convert("A", 2))