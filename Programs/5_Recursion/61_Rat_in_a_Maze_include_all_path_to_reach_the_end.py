# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1 , Medium

# Recursive Tree
# https://0x0.st/Hw4x.839.png

# Brute
# T.C. - O(4^n)
# S.C  - O(n)


class Solution:
    def solve(self, x, y, mat, n, path, seen, ans):
        if x < 0 or y < 0:
            return

        if x >= n or y >= n:
            return

        if mat[x][y] == 0:
            return

        if seen[(x, y)]:
            return

        if x == n - 1 and y == n - 1:
            ans.append(path[:])
            return

        dirs = [(1, 0, "D"), (0, 1, "R"), (-1, 0, "U"), (0, -1, "L")]

        for dx, dy, dir in dirs:
            seen[(x, y)] = True
            self.solve(x + dx, y + dy, mat, n, path + dir, seen, ans)
            seen[(x, y)] = False

    def findPath(self, m, n):
        ans = []
        seen = {}
        for i in range(n):
            for j in range(n):
                seen[(i, j)] = False
        self.solve(0, 0, m, n, "", seen, ans)
        return ans


obj = Solution()
N = 4
ls = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
k = obj.findPath(ls, N)
print(k)
