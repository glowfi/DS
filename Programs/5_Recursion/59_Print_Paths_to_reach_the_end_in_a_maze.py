# NA , Medium

# Brute
# T.C. - O(2^n)
# S.C  - O(n)+O(m*n)


# Only right(R) , down(D), diagnonal(d) direction
class Solution:
    def solve(self, x, y, m, n, cache, path, ans):
        if x >= m or y >= n:
            return 0

        if x < 0 or y < 0:
            return 0

        if x == m - 1 and y == n - 1:
            ans.append(path[:])
            return 1

        # Go right
        self.solve(x, y + 1, m, n, cache, path + "R", ans)

        # Go down
        self.solve(x + 1, y, m, n, cache, path + "D", ans)

        # Go diagonal
        self.solve(x + 1, y + 1, m, n, cache, path + "d", ans)

    def uniquePaths(self, m: int, n: int):
        cache = {}
        ans = []
        self.solve(0, 0, m, n, cache, "", ans)
        return ans


obj = Solution()
print(obj.uniquePaths(3, 3))
