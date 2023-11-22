# https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1 , Medium

# Brute [Recursion]
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, sm, arr):
        if idx == len(arr):
            if sm == 0:
                return True
            return False

        # Take
        if self.helper(idx + 1, sm - arr[idx], arr):
            return True

        # Not Take
        if self.helper(idx + 1, sm, arr):
            return True

        return False

    def isSubsetSum(self, N, arr, sum):
        return self.helper(0, sum, arr)


# Better [Memoization]
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, sm, arr, cache):
        if idx == len(arr):
            if sm == 0:
                return True
            return False

        if str(idx) + str(sm) in cache:
            return cache[str(idx) + str(sm)]

        # Take
        take = self.helper(idx + 1, sm - arr[idx], arr, cache)

        # Not Take
        notTake = self.helper(idx + 1, sm, arr, cache)

        cache[str(idx) + str(sm)] = take or notTake

        return cache[str(idx) + str(sm)]

    def isSubsetSum(self, N, arr, sum):
        return self.helper(0, sum, arr, {})
