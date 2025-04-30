# https://leetcode.com/problems/insert-interval , Medium


# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(1)


from typing import List


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

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        ans: list[list[int]] = []

        # Find the interval with closest start time [lower bound]
        idx = 0
        while idx < len(intervals) and intervals[idx][0] <= newInterval[0]:
            ans.append(intervals[idx])
            idx += 1

        # Insert just after the closes start time
        ans.append(newInterval)

        # Insert remaining
        for i in range(idx, len(intervals)):
            ans.append(intervals[i])

        # Then do merge overlapping intervals
        return self.merge(ans)
