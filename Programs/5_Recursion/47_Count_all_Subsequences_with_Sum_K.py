# https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1 , Medium

# Recursive Tree
# https://0x0.st/Hth7.226.png

# Brute [Recursion] [ans in body]
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, sm, arr):
        if idx == len(arr):
            if sm == 0:
                return 1
            return 0

        MOD = (10**9) + 7

        # Take
        take = self.helper(idx + 1, sm - arr[idx], arr) % MOD

        # Not Take
        nottake = self.helper(idx + 1, sm, arr) % MOD

        return (take + nottake) % MOD

    def perfectSum(self, arr, n, sum):
        return self.helper(0, sum, arr)


# Better [Memoization]
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, sm, arr, cache):
        if idx == len(arr):
            if sm == 0:
                return 1
            return 0

        if str(idx) + str(sm) in cache:
            return cache[str(idx) + str(sm)]

        MOD = (10**9) + 7

        # Take
        take = self.helper(idx + 1, sm - arr[idx], arr, cache) % MOD

        # Not Take
        nottake = self.helper(idx + 1, sm, arr, cache) % MOD

        cache[str(idx) + str(sm)] = (take + nottake) % MOD

        return cache[str(idx) + str(sm)]

    def perfectSum(self, arr, n, sum):
        return self.helper(0, sum, arr, {})
