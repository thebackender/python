#https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        def fromBinary(s):
            num = 0
            for i in range(len(s)):
                n = len(s) - i - 1
                num += pow(2, n)*int(s[i])
            return num
        summ = fromBinary(a) + fromBinary(b)
        string = ""
        while int(summ/2):
            string += str(int(summ%2))
            summ = int(summ/2)
        string += str(summ)
        return string[::-1]
        """
        return bin(int(a, 2) + int(b, 2))[2:]
print(Solution().addBinary("1010", "1011"))