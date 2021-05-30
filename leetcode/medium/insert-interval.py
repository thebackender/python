#https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                intervals[i] = None
        return [a for a in intervals if a]
print(Solution().insert([], [4,8]))