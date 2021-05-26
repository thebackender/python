#https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):
        digits.insert(0, 0)
        new = digits[::-1]
        for i in range(len(new)):
            if new[i] != 9:
                new[i] += 1
                break
            else:
                new[i] = 0
        arr = new[::-1]
        if arr[0] == 0:
            arr.pop(0)
        return arr
print(Solution().plusOne([9,9,9]))