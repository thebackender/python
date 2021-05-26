#https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int):
        l = list()
        for i in range(1, numRows+1):
            n = [1]*i
            if i > 2:
                for j in range(1, int((i/2) + (i%2))):
                    n[j] = l[i-2][j-1] + l[i-2][j]
                    n[-j-1] = n[j]
            l.append(n)
        return l
print(Solution().generate(11))