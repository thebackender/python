#https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height) -1
        most = 0
        while i<j:
            if height[i] < height[j]:
                area = (j-i)*height[i]
                i+=1
            elif height[i] > height[j]:
                area = (j-i)*height[j]
                j-=1
            else:
                area = (j-i)*height[i]
                i+=1
                j-=1
            most = max(most, area)
        return most
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
#Understanding new solution: will come from front and back
"""
Time limit:
n = len(height)
most = 0
for i in range(n):
    for j in range(i+1, n):
        most = max(min(height[i], height[j])*(j-i), most)
return most
"""