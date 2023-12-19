# https://leetcode.com/problems/surrounded-regions/ , Medium

# Optimal
# T.C. - O(N) + O(M) + O(NxMx4)
# S.C  - O(N x M), O(N x M)


class Solution:
    def check_in_bounds(self, board, ro, co):
        if ro < 0 or co < 0:
            return False
        if ro >= len(board) or co >= len(board[0]):
            return False
        return True

    def dfs(self, ro, co, board, seen):
        if (
            not self.check_in_bounds(board, ro, co)
            or board[ro][co] == "X"
            or (ro, co) in seen
        ):
            return

        seen[(ro, co)] = True
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dx, dy in dirs:
            self.dfs(dx + ro, dy + co, board, seen)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        r, c = len(board), len(board[0])
        seen = {}

        # First row
        for i in range(c):
            if board[0][i] == "O" and (0, i) not in seen:
                self.dfs(0, i, board, seen)

        # Last row
        for i in range(c):
            if board[r - 1][i] == "O" and (r - 1, i) not in seen:
                self.dfs(r - 1, i, board, seen)

        # First Column
        for i in range(r):
            if board[i][0] == "O" and (i, 0) not in seen:
                self.dfs(i, 0, board, seen)

        # Last Column
        for i in range(r):
            if board[i][c - 1] == "O" and (i, c - 1) not in seen:
                self.dfs(i, c - 1, board, seen)

        for i in range(r):
            for j in range(c):
                if (i, j) not in seen and board[i][j] == "O":
                    board[i][j] = "X"

        return board
