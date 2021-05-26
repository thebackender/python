#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str):
        if digits == "":
            return []
        d = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        n = len(digits)
        if n == 1:
            return d[digits]
        arr = []
        if n == 2:
            for a in d[digits[0]]:
                for b in d[digits[1]]:
                    arr.append(a+b)
        if n == 3:
            for a in d[digits[0]]:
                for b in d[digits[1]]:
                    for c in d[digits[2]]:
                        arr.append(a+b+c)
        if n == 4:
            for a in d[digits[0]]:
                for b in d[digits[1]]:
                    for c in d[digits[2]]:
                        for r in d[digits[3]]:
                            arr.append(a+b+c+r)
        return arr
print(Solution().letterCombinations("2456"))