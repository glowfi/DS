# https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1 , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, sm, arr):
        if idx == len(arr):
            if sm == 0:
                return 1
            return 0

        if self.helper(idx + 1, sm - arr[idx], arr) == 1:
            return 1

        return self.helper(idx + 1, sm, arr)

    def isSubsetSum(self, N, arr, sum):
        return self.helper(0, sum, arr)
