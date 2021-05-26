#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers, target: int):
        i = 0
        j = len(numbers) - 1
        n = len(numbers)
        while i < n and j > 0:
            add = numbers[i]+numbers[j]
            if add == target:
                return [i+1, j+1]
            elif add > target:
                j -= 1
            else:
                i += 1
print(Solution().twoSum([2,3,4], 6))