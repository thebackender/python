#https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        def convert(word):
            result = ""
            count = 1
            starter = word[0]
            for letter in word[1:]:
                if letter != starter:
                    result += str(count) + starter
                    starter = letter
                    count = 1
                else:
                    count += 1
            result += str(count) + starter
            return result
        result = "1"
        for _ in range(n-1):
            result = convert(result)
        return result
print(Solution().countAndSay(3))