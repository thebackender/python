class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        arr = sorted(nums1 + nums2)
        n = len(arr)
        a = 0
        if n%2 == 1:
            a = arr[n//2]
        else:
            a = (arr[n//2] + arr[n//2 - 1])/2
        return float("%.5f" % a)
print(Solution().findMedianSortedArrays([1], [3, 4]))