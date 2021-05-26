#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            arr = []
            while int(x%10) or int(x/10):
                arr.append(x%10)
                x = int(x/10)
            for i in range(int(len(arr)/2)):
                if arr[i] != arr[len(arr) - i - 1]:
                    return False
            return True
        else:
            return False
c = Solution()
print(c.isPalindrome(101))