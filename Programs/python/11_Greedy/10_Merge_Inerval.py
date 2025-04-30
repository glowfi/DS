# https://leetcode.com/problems/merge-intervals , Medium


# Optimal
# T.C. - O(nlog(n))+O(n)
# S.C  - O(1)

# Selection criteria : Sort the interval based on start time
# Keep track of prev interval and check overlap with current interval


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        prev_interval = intervals[0]
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if prev_interval[-1] >= intervals[i][0]:
                prev_interval = [
                    min(intervals[i][0], prev_interval[0]),
                    max(intervals[i][-1], prev_interval[-1]),
                ]
                ans[-1] = prev_interval
            else:
                prev_interval = intervals[i]
                ans.append(prev_interval)

        return ans
