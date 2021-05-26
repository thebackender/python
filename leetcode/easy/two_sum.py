#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
c = Solution()
print(c.twoSum([3,2,4], 6))