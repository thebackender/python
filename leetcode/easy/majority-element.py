#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums) -> int:
        for a in set(nums):
            if nums.count(a) > len(nums)/2:
                return a
print(Solution().majorityElement([2,2,1,1,1,2,2]))