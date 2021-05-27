#https://leetcode.com/problems/permutations/
from itertools import permutations
class Solution:
    def permute(self, nums):
        perm = permutations(nums)
        arr = []
        for i in list(perm):
            arr.append(list(i))
        return arr
print(Solution().permute([1,2,3]))