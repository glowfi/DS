# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1,Medium

# Brute
# T.C. -> O(n^2)
# S.C. -> O(n)


class Solution:
    def maxLen(self, n, arr):
        mx = 0
        for i in range(len(arr)):
            sum = 0
            for j in range(i, len(arr)):
                sum += arr[j]
                if sum == 0:
                    mx = max(mx, j - i + 1)
        return mx


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def maxLen(self, n, arr):
        h = {0: -1}
        pref = 0
        mx = 0

        for i in range(len(arr)):
            pref += arr[i]
            if pref in h:
                mx = max(mx, i - h[pref])

            if pref not in h:
                h[pref] = i
        return mx
