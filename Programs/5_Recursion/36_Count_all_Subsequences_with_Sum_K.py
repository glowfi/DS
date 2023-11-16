# https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1 , Medium

# Recursive Tree
# https://0x0.st/Hth7.226.png

# Brute [ans in argument]
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, arr, sum, res):
        if idx == len(arr):
            if sum == 0:
                res[0] += 1
                return
            return

        # Take
        self.helper(idx + 1, arr, sum - arr[idx], res)

        # notTake
        self.helper(idx + 1, arr, sum, res)

    def perfectSum(self, arr, n, sum):
        res = [0]

        self.helper(0, arr, sum, res)

        return res[0]


# Brute [ans in body]
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def helper(self, idx, arr, sum):
        MOD = (10**9) + 7

        if idx == len(arr):
            if sum == 0:
                return 1
            return 0

        # Take
        take = 0
        if arr[idx] <= sum:
            take = self.helper(idx + 1, arr, sum - arr[idx]) % MOD

        # notTake
        notTake = self.helper(idx + 1, arr, sum) % MOD

        return (take + notTake) % MOD

    def perfectSum(self, arr, n, sum):
        return self.helper(0, arr, sum)
