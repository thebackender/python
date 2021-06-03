#https://leetcode.com/problems/sort-colors/
def b(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
class Solution:
    def sortColors(self, nums):
        bubbleSort(nums)