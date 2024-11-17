# https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1,Medium

# Brute
# T.C. -> O(n^2)
# S.C. -> O(n)


class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        mx = 0
        for i in range(len(arr)):
            s = 0
            for j in range(i, len(arr)):
                s += arr[j]
                if s == k:
                    mx = max(mx, j - i + 1)
        return mx


# Better
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        mx = 0
        h = {0: -1}
        pref = 0

        for i in range(len(arr)):
            pref += arr[i]
            remaining = pref - k

            if remaining in h:
                mx = max(mx, i - h[remaining])

            if pref not in h:
                h[pref] = i

        return mx


# Optimal
# T.C. -> O(2n)
# S.C. -> O(1)


class Solution:
    def lenOfLongestSubarr(self, arr, k):
        l, r = 0, 0
        n = len(arr)
        sm = 0
        mx_len = 0

        while r < n:
            sm += arr[r]

            while sm > k:
                sm -= arr[l]
                l += 1

            if sm == k:
                mx_len = max(mx_len, r - l + 1)

            r += 1

        return mx_len
