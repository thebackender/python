#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums):
        nums.sort()
        arr = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add == 0:
                    r = [nums[i], nums[j], nums[k]]
                    if r not in arr:
                        arr.append(r)
                    j += 1
                    k -= 1
                elif add < 0:
                    j += 1
                elif add > 0:
                    k -= 1
        return arr
print(Solution().threeSum([0]))