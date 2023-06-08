# https://leetcode.com/problems/merge-intervals/ , Medium

# Brute
# T.C. -> O(n*n)+O(nlog(n))
# S.C. -> O(no of intervals)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()

        for i in range(len(intervals)):
            if len(ans) > 0 and ans[-1][1] >= intervals[i][1]:
                continue
            ans.append(intervals[i])

            for j in range(i + 1, len(intervals)):
                if intervals[j][0] > ans[-1][1]:
                    break

                if intervals[j][0] <= ans[-1][1]:
                    ans[-1] = [ans[-1][0], max(intervals[j][1], ans[-1][1])]

        return ans


# Optimal
# T.C. -> O(n)+O(nlog(n))
# S.C. -> O(no of intervals)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for i in range(len(intervals)):
            if len(ans) == 0 or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])

            elif ans[-1][1] >= intervals[i][0]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], intervals[i][1])]
        return ans
