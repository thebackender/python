#https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums) -> int:
        n = len(nums) - 1
        while n > 0:
            val = nums[n]
            nums.remove(val)
            try:
                nums.remove(val)
            except:
                return val
            n = len(nums) - 1
        return nums[0]
print(Solution().singleNumber([4,1,2,1,2]))
"""
#faster version
j = len(nums)-1
while(j>0):
    val = nums[j]
    nums.pop(j)
    try:
        nums.pop(nums.index(val))
    except:
        return val
    j = len(nums)-1
return nums[0]
"""