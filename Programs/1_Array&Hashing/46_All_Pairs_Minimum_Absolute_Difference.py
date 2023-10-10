# https://leetcode.com/problems/minimum-absolute-difference/,Easy


# Optimal
# T.C. -> O(n*k)
# S.C. -> O(1)


class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        mn = float("inf")
        out = []

        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) <= mn:
                mn = abs(arr[i] - arr[i + 1])
                while out and mn != abs(out[-1][0] - out[-1][1]):
                    out.pop(-1)
                out.append([arr[i], arr[i + 1]])
        return out
