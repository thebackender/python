class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return []
        if len(set(nums)) == 1:
            return len(nums)
        a = 0
        arr = [0]
        for i in set(nums):
            num = nums.count(i)
            if num > max(arr):
                a = i
            arr.append(num)
        arr.sort()
        for _ in range(arr[-1] - arr[-2]):
            nums.remove(a)
        return len(nums)
print(Solution().removeDuplicates([1]))