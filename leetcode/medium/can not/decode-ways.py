#https://leetcode.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        count = 0
        if s[0] == "0":
            return 0
        print(ord("Z"))
        return chr(65)
print(Solution().numDecodings("12"))