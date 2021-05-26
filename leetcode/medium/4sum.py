#https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums, target: int):
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    
                first_part = nums[i] + nums[j]     
                l, r = j + 1, n - 1
                while l < r:
                    total = first_part + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1
                        
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        
        return res
print(Solution().fourSum([1,0,-1,0,-2,2], 0))