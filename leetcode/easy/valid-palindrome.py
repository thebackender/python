#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for a in s:
            if a in "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                string += a
        string = string.lower()
        for i in range(int(len(string)/2)):
            if string[i] != string[len(string) - 1 - i]:
                return False
        return True
print(Solution().isPalindrome("race a car"))