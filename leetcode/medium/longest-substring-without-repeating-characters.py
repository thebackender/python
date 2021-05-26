#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        longest = 1
        arr = []
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if s[j] not in arr:
                    arr.append(s[j])
                else:
                    longest = max(len(arr), longest)
                    arr = []
                    break
        return longest
print(Solution().lengthOfLongestSubstring('au'))