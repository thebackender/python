#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums, target: int):
        if target not in nums:
            return [-1, -1]
        arr = []
        i = 0
        for i, a in enumerate(nums):
            if a == target:
                arr.append(i)
        return [arr[0], arr[len(arr) - 1]]
print(Solution().searchRange([5,7,7,8,8,10], 8))