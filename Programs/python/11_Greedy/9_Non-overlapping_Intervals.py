# https://leetcode.com/problems/non-overlapping-intervals , Medium


# Optimal
# T.C. - O(nlog(n))
# S.C  - o(1)

# Selection criteria : Select the interval that ending time is less
# Keep track of prev interval and check overlap with current interval


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        c = 0

        prev_interval = intervals[0]
        for i in range(1, len(intervals)):
            if prev_interval[-1] > intervals[i][0]:
                c += 1
            else:
                prev_interval = intervals[i]

        return c
