#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for _ in range(n)]   
        longest = ""
        for i in range(n):
            for j in range(n - i):
                if (i == 0) or (i == 1 and s[j] == s[j+i]) or (s[j] == s[j+i] and dp[i-2][j+1]):
                    dp[i][j] = 1
                    longest = s[j:j+i+1]
        return longest
print(Solution().longestPalindrome("fasdabadpao"))
"""
Time exceeded:
l = len(s)
longest = s[0]
if l == 1 or l == len(set(s)):
    return longest
def isPol(a):
    n = len(a)
    for i in range((n + n%2)//2):
        if a[i] != a[n - i - 1]:
            return False
    return True
for i in range(l):
    for j in range(i+1, l):
        sub = s[i:j+1]
        if isPol(sub):
            if len(sub) > len(longest):
                longest = sub
return longest
"""