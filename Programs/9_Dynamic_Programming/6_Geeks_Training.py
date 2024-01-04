# https://www.geeksforgeeks.org/problems/geeks-training/1 , Medium

# Recursion
# T.C. - O(N*4*3)
# S.C  - O(N)


class Solution:
    def solve(self, day, prev, points):
        if day == 0:
            mx_points = float("-inf")
            for task_index in range(len(points[0])):
                if task_index != prev:
                    mx_points = max(mx_points, points[day][task_index])
            return mx_points

        mx_points = 0

        for task_index in range(len(points[0])):
            if task_index != prev:
                val = self.solve(day - 1, task_index, points)
                if val + points[day][task_index] > mx_points:
                    mx_points = val + points[day][task_index]

        return mx_points

    def maximumPoints(self, points, n):
        return self.solve(n - 1, -1, points)


# Memoization
# T.C. - O(N*4*3)
# S.C  - O(N) + O(N*4)


class Solution:
    def solve(self, day, prev, points, dp):
        if (day, prev) in dp:
            return dp[(day, prev)]

        if day == 0:
            mx_points = float("-inf")
            for task_index in range(len(points[0])):
                if task_index != prev:
                    mx_points = max(mx_points, points[day][task_index])
            return mx_points

        mx_points = 0

        for task_index in range(len(points[0])):
            if task_index != prev:
                val = self.solve(day - 1, task_index, points, dp)
                if val + points[day][task_index] > mx_points:
                    mx_points = val + points[day][task_index]

        dp[(day, prev)] = mx_points

        return dp[(day, prev)]

    def maximumPoints(self, points, n):
        dp = {}
        return self.solve(n - 1, -1, points, dp)


# Tabulation
# T.C. - O(N*4*3)
# S.C  - O(N*4)


class Solution:
    def maximumPoints(self, points, n):
        dp = [[0 for _ in range(4)] for _ in range(len(points))]

        dp[0][0] = max(points[0][1], points[0][2])
        dp[0][1] = max(points[0][2], points[0][0])
        dp[0][2] = max(points[0][0], points[0][1])

        # dp[0][-1] -> if there is only one day and start is -1 basically we want answer for dp[n-1][-1] n-1th day and last day is -1.
        dp[0][3] = max(points[0][0], points[0][1], points[0][2])

        for day in range(1, n):
            for prev in range(4):
                mx = float("-inf")
                for task_index in range(len(points[0])):
                    if task_index != prev:
                        currPoint = dp[day - 1][task_index]
                        mx = max(mx, currPoint + points[day][task_index])
                dp[day][prev] = mx

        return dp[n - 1][3]


# Space Optimized
# T.C. - O(N*4*3)
# S.C  - O(4)


class Solution:
    def maximumPoints(self, points, n):
        dp = [0 for _ in range(4)]

        dp[0] = max(points[0][1], points[0][2])
        dp[1] = max(points[0][2], points[0][0])
        dp[2] = max(points[0][0], points[0][1])

        # dp[0][-1] -> if there is only one day and start is -1 basically we want answer for dp[n-1][-1] n-1th day and last day is -1.
        dp[3] = max(points[0][0], points[0][1], points[0][2])

        for day in range(1, n):
            tmp = [0 for _ in range(4)]
            for prev in range(4):
                mx = float("-inf")
                for task_index in range(len(points[0])):
                    if task_index != prev:
                        currPoint = dp[task_index]
                        mx = max(mx, currPoint + points[day][task_index])
                tmp[prev] = mx
            dp = tmp

        return dp[3]
