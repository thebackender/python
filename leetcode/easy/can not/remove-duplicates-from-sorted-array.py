#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums) -> int:
        return len(set(nums))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))