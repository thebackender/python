#https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)
print(Solution().searchInsert([1,3,5,6], 2))