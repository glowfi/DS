# https://leetcode.com/problems/unique-paths/ , Medium

# Recursive Tree
# https://0x0.st/HwWl.018.png

# Brute [Recursive]
# T.C. - O(2^n)
# S.C  - O(n)


class Solution:
    def solve(self, x, y, m, n) -> int:
        if x >= m or x < 0:
            return 0

        if y >= n or y < 0:
            return 0

        if x == m - 1 and y == n - 1:
            return 1

        # Go right
        right = self.solve(x, y + 1, m, n)

        # Go down
        down = self.solve(x + 1, y, m, n)

        return right + down

    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(0, 0, m, n)


# Better [Memoized]
# T.C. - O(n)
# S.C  - O(n)+O(m*n)


class Solution:
    def solve(self, x, y, m, n, cache) -> int:
        if x >= m or y >= n:
            return 0

        if (x, y) in cache:
            return cache[(x, y)]

        if x == m - 1 and y == n - 1:
            return 1

        # Go right
        right = self.solve(x, y + 1, m, n, cache)

        # Go down
        down = self.solve(x + 1, y, m, n, cache)

        cache[(x, y)] = right + down

        return cache[(x, y)]

    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.solve(0, 0, m, n, cache)
