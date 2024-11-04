# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1 , Easy

# Brute
# T.C. - O(N-k*k)
# S.C  - O(1)


class Solution:

    def maximumSumSubarray(self, arr, k):
        mxSm = float("-inf")
        for i in range(len(arr) - k + 1):
            sm = 0
            for j in range(i, i + k):
                sm += arr[j]
            mxSm = max(sm, mxSm)
        return mxSm


# Optimal
# T.C. - O(N)
# S.C  - O(1)


class Solution:

    def maximumSumSubarray(self, arr, k):
        l, r = 0, -1
        sm = 0
        for i in range(k):
            sm += arr[i]
            r += 1
        mxSm = max(float("-inf"), sm)

        while r < len(arr) - 1:
            # Remove calculations
            sm -= arr[l]
            l += 1

            # Add incoming
            r += 1
            sm += arr[r]

            mxSm = max(mxSm, sm)

        return mxSm
