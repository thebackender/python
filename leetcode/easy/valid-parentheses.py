#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        opens = []
        def find_by_value(a, brackets):
            for o, c in brackets.items():
                if a == c:
                    return o
        for a in s:
            if a in brackets:
                opens.append(a)
            elif find_by_value(a, brackets) in opens:
                if a == brackets[opens[-1]]:
                    del opens[-1]
                else:
                    return False
            else:
                return False
        if len(opens) == 0:
            return True
        else:
            return False
print(Solution().isValid("["))
