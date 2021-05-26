#https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        n = len(nums)
        nums.sort()
        result = target
        difference = float('inf')
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add == target:
                    return target
                if abs(add-target) < difference:
                    difference = abs(add-target)
                    result = add
                if add < target:
                    j += 1
                elif add > target:
                    k -= 1
        return result
print(Solution().threeSumClosest([1,2,0], 3))
"""
Time limit:
nums.sort()
arr = [target]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j+1, len(nums)):
            add = nums[i] + nums[j] + nums[k]
            if add not in arr:
                arr.append(add)
arr.sort()
a = arr.index(target)
arr.pop(a)
if len(arr) == 1:
    return arr[0]
return min(abs(arr[a-1] - target), abs(arr[a] - target)) + target
"""