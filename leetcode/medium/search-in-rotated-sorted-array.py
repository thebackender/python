#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums, target: int) -> int:
        if target not in nums:
            return -1
        i = 0
        for i, a in enumerate(nums):
            if a == target:
                return i
print(Solution().search([4,5,6,7,0,1,2], 0))