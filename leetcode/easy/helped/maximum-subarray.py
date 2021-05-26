#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*n #[0,0,0,0,0,0,]
        dp[0]=nums[0]
        maxnum=nums[0]
        for i in range(1,n):
            dp[i]=max(nums[i],nums[i]+dp[i-1])
            maxnum=max(maxnum,dp[i])
        return maxnum
print(Solution().maxSubArray([-1,5,4]))