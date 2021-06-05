#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums, target: int) -> bool:
        if target in nums:
            return True
        else:
            return False
print(Solution().search([2,5,6,0,0,1,2], 3))