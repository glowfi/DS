# https://leetcode.com/problems/n-queens/ , Hard

# Brute
# T.C. - O(n^n)
# S.C  - O(n)


class Solution:
    def canBePlaced(self, row, col, mat, n):
        # Copy
        rw = row
        cl = col

        # Upwards
        while rw >= 0:
            if mat[rw][cl] == "Q":
                return False
            rw -= 1

        # Copy
        rw = row
        cl = col

        # Upper Left
        while rw >= 0 and cl >= 0:
            if mat[rw][cl] == "Q":
                return False
            rw -= 1
            cl -= 1

        # Copy
        rw = row
        cl = col

        # Upper Right
        while rw < n and cl < n:
            if mat[rw][cl] == "Q":
                return False
            rw -= 1
            cl += 1

        return True

    # def display(self, mat):
    #     for i in range(len(mat)):
    #         for j in range(len(mat[0])):
    #             print(mat[i][j], end=" ")
    #         print()
    #     print("")

    def solve(self, row, n, mat, ans):
        if row == n:
            ls = []
            for i in range(len(mat)):
                tmp = ""
                for j in range(len(mat[0])):
                    tmp += mat[i][j]
                ls.append(tmp[:])

            ans.append(ls)
            return

        for col in range(n):
            if self.canBePlaced(row, col, mat, n):
                mat[row][col] = "Q"
                self.solve(row + 1, n, mat, ans)
                mat[row][col] = "."

    def solveNQueens(self, n: int) -> list[list[str]]:
        mat = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        self.solve(0, n, mat, ans)
        return ans


obj = Solution()
print(obj.solveNQueens(4))
