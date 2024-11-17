# https://leetcode.com/problems/game-of-life/ , Medium

# Brute
# T.C. - O(n*m)+O(n*m)
# S.C  - O(n*m)


class Solution:
    def getNeighbourCount(self, board, i, j):
        dirs = [(1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, -1)]
        count = 0
        rows, cols = len(board), len(board[0])

        for x, y in dirs:
            dx, dy = x + i, y + j
            if 0 <= dx < rows and 0 <= dy < cols and abs(board[dx][dy]) == 1:
                count += 1

        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # Create a copy of the board to store the next state
        new_board = [[0 for j in range(cols)] for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                neighbour_count = self.getNeighbourCount(board, i, j)

                if board[i][j] == 1:
                    # Live cell with 2 or 3 live neighbours stays alive
                    if neighbour_count == 2 or neighbour_count == 3:
                        new_board[i][j] = 1
                else:
                    # Dead cell with 3 live neighbours becomes alive
                    if neighbour_count == 3:
                        new_board[i][j] = 1

        # Update the original board with the new state
        for i in range(rows):
            for j in range(cols):
                board[i][j] = new_board[i][j]


# Optimal
# T.C. - O(n*m)+O(n*m)
# S.C  - O(1)

# 0 -> 0: 0
# 1 -> 1: 1
# 0 -> 1: 2
# 1 -> 0: 3


class Solution:
    def getNeighbourCount(self, board, i, j):
        dirs = [(1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, -1)]
        count = 0
        rows, cols = len(board), len(board[0])

        for x, y in dirs:
            dx, dy = x + i, y + j
            if 0 <= dx < rows and 0 <= dy < cols and board[dx][dy] in [1, 3]:
                count += 1

        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                neighbour_count = self.getNeighbourCount(board, i, j)

                if board[i][j] == 1:
                    # Live cell with 2 or 3 live neighbours stays alive
                    if neighbour_count == 2 or neighbour_count == 3:
                        board[i][j] = 3
                else:
                    # Dead cell with 3 live neighbours becomes alive
                    if neighbour_count == 3:
                        board[i][j] = 2

        # Update the original board with the new state
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1
