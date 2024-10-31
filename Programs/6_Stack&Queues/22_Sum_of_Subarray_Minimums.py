# https://leetcode.com/problems/sum-of-subarray-minimums , Medium

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        sm = 0

        for i in range(len(arr)):
            mn = arr[i]
            for j in range(i + 1, len(arr)):
                mn = min(arr[j], mn)
                sm += mn
            sm += arr[i]

        return sm


# Optimal
# T.C. - O(5N)
# S.C  - O(5N)


class Solution:
    def sumSubarrayMins(self, arr):
        MOD = (10**9) + 7
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stk = []

        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop(-1)

            if stk:
                left[i] = stk[-1]

            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop(-1)

            if stk:
                right[i] = stk[-1]

            stk.append(i)

        sm = 0
        for i in range(n):
            sm = (sm + ((i - left[i]) * (right[i] - i) * arr[i]) % MOD) % MOD

        return sm
