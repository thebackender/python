#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip().lstrip()
        if s == "":
            return 0
        elif " " not in s:
            return len(s)
        else:
            c = 0
            while s[-1] != " ":
                s = s[:-1]
                c += 1
            return c
print(Solution().lengthOfLastWord("   dhe asdfasdf"))