#https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int):
        opened = closed = n
        return self.returnParenthesis([], '', opened, closed)
    def returnParenthesis(self, result, currentStr, opened, closed):
      if opened == 0 and closed == 0:
        result.append(currentStr)
      elif opened == 0:
        self.returnParenthesis(result, currentStr+')', opened, closed-1)
      elif opened == closed:
        self.returnParenthesis(result, currentStr+'(', opened-1, closed)
      else:
        self.returnParenthesis(result, currentStr+'(', opened-1, closed)
        self.returnParenthesis(result, currentStr+')', opened, closed-1)
      return result
print(Solution().generateParenthesis(3))