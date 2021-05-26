#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs):
        s = ""
        for a in range(len(min(strs, key=len))):
            for b in strs:
                if b[a] != min(strs, key=len)[a]:
                    return s
            s += min(strs, key=len)[a]
        return s
c = Solution()
print(c.longestCommonPrefix(["flower","flow","flight"]))