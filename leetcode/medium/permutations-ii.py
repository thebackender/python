#https://leetcode.com/problems/permutations-ii/
from itertools import permutations
class Solution:
    def permute(self, nums):
        perm = permutations(nums)
        arr = []
        for i in list(perm):
            if list(i) not in arr:
                arr.append(list(i))
        return arr
print(Solution().permute([1,1,2]))