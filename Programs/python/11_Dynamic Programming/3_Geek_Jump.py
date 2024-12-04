# https://www.geeksforgeeks.org/problems/geek-jump/1 , Easy

# Recursion
# T.C. - O(2^n)
# S.C  - O(n)


from types import prepare_class


class Solution:
    def solve(self, n, height, k):
        if n == 0:
            return 0

        min_energy = float("inf")

        for step in range(1, k + 1):
            if n - step >= 0:
                val = self.solve(n - step, height, k)
                if val + abs(height[n] - height[n - step]) < min_energy:
                    min_energy = val + abs(height[n] - height[n - step])

        return min_energy

    def minimumEnergy(self, height, n):
        k = 2
        return self.solve(n - 1, height, k)


# Memoization
# T.C. - O(n)
# S.C  - O(n)+O(n)


class Solution:
    def solve(self, n, height, dp, k):
        if n == 0:
            return 0

        if n in dp:
            return dp[n]

        min_energy = float("inf")

        for step in range(1, k + 1):
            if n - step >= 0:
                val = self.solve(n - step, height, dp, k)
                if val + abs(height[n] - height[n - step]) < min_energy:
                    min_energy = val + abs(height[n] - height[n - step])

        dp[n] = min_energy

        return dp[n]

    def minimumEnergy(self, height, n):
        dp = {}
        k = 2
        return self.solve(n - 1, height, dp, k)


# Tabulation
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def minimumEnergy(self, height, n):
        dp = {i: 0 for i in range(n)}
        dp[0] = 0
        k = 2

        for i in range(1, n):
            min_energy = float("inf")
            for step in range(1, k + 1):
                if i - step >= 0:
                    val = dp[i - step]
                    min_energy = min(
                        val + abs(height[i] - height[i - step]), min_energy
                    )
            dp[i] = min_energy

        return dp[n - 1]


n = 4
height = [10, 20, 30, 10]

n = 8
height = [7, 4, 4, 2, 6, 6, 3, 4]
obj = Solution()
print(obj.minimumEnergy(height, n))
