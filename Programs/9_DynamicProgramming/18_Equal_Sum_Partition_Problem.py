# https://leetcode.com/problems/partition-equal-subset-sum/ , Medium

# Recursion
# T.C. - O(n*target*2^n)+O(n)
# S.C  - O(n)


class Solution:
    def solve(self, arr, target, N):
        if target == 0:
            return True

        if N == 0:
            if arr[0] == target:
                return True
            return False

        take, notTake = False, False

        if arr[N] <= target:
            take = self.solve(arr, target - arr[N], N - 1)
            notTake = self.solve(arr, target, N - 1)

        elif arr[N] > target:
            notTake = self.solve(arr, target, N - 1)

        return take or notTake

    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)

        if sm % 2 != 0:
            return False
        else:
            return self.solve(nums, sm // 2, len(nums) - 1)


# Memoization
# T.C. - O(n*target)+O(n)
# S.C  - O(n*target)+O(n)


class Solution:
    def solve(self, arr, target, N):
        if (N, target) in self.dp:
            return self.dp[(N, target)]

        if target == 0:
            return True

        if N == 0:
            if arr[0] == target:
                return True
            return False

        take, notTake = False, False

        if arr[N] <= target:
            take = self.solve(arr, target - arr[N], N - 1)
            notTake = self.solve(arr, target, N - 1)

        elif arr[N] > target:
            notTake = self.solve(arr, target, N - 1)

        self.dp[(N, target)] = take or notTake

        return take or notTake

    def canPartition(self, nums: List[int]) -> bool:
        self.dp = {}
        sm = sum(nums)

        if sm % 2 != 0:
            return False
        else:
            return self.solve(nums, sm // 2, len(nums) - 1)


# Tabulation
# T.C. - O(n*target)+O(n)
# S.C  - O(n*target)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        n = len(nums)
        dp = [[False for _ in range(sm + 1)] for _ in range(n)]

        if sm % 2 != 0:
            return False
        else:
            for N in range(n):
                for target in range(sm + 1):
                    if target == 0:
                        dp[N][target] = True
                    elif N == 0:
                        if nums[0] == target:
                            dp[N][target] = True
                        else:
                            dp[N][target] = False
                    else:
                        take, notTake = False, False
                        if nums[N] <= target:
                            take = dp[N - 1][target - nums[N]]
                            notTake = dp[N - 1][target]

                        elif nums[N] > target:
                            notTake = dp[N - 1][target]

                        dp[N][target] = take or notTake

            return dp[n - 1][sm // 2]


# Space Optimized
# T.C. - O(n*target)+O(n)
# S.C  - O(target)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        n = len(nums)
        dp = [False for _ in range(sm + 1)]

        if sm % 2 != 0:
            return False
        else:
            for N in range(n):
                tmp = [False for _ in range(sm + 1)]
                for target in range(sm + 1):
                    if target == 0:
                        tmp[target] = True
                    elif N == 0:
                        if nums[0] == target:
                            tmp[target] = True
                        else:
                            tmp[target] = False
                    else:
                        take, notTake = False, False
                        if nums[N] <= target:
                            take = dp[target - nums[N]]
                            notTake = dp[target]

                        elif nums[N] > target:
                            notTake = dp[target]

                        tmp[target] = take or notTake
                dp = tmp

            return dp[sm // 2]
