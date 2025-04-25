# https://leetcode.com/problems/cherry-pickup/ , Hard


# Backtracking
# T.C. - O(all_path_from_top_left_to_bottom_right*all_path_from_bottom_right_to_top_left)
# S.C  - O(path_top_left+path_bottom_right)


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve1(self, ro, co, cherries_collected_so_far, grid):
        if (
            not self.check_in_bounds(ro, co, len(grid), len(grid[0]))
            or grid[ro][co] == -1
        ):
            return 0

        if ro == len(grid) - 1 and co == len(grid[0]) - 1:
            cherry_value = grid[ro][co]

            if cherry_value == 1:
                grid[ro][co] = 0
                self.solve2(ro, co, cherries_collected_so_far + 1, grid)
            else:
                self.solve2(ro, co, cherries_collected_so_far, grid)

            grid[ro][co] = cherry_value
            return

        cherry_value = grid[ro][co]

        if cherry_value == 1:
            grid[ro][co] = 0
        self.solve1(ro + 1, co, cherries_collected_so_far + cherry_value, grid)
        self.solve1(ro, co + 1, cherries_collected_so_far + cherry_value, grid)
        grid[ro][co] = cherry_value

    def solve2(self, ro, co, cherries_collected_so_far, grid):
        if (
            not self.check_in_bounds(ro, co, len(grid), len(grid[0]))
            or grid[ro][co] == -1
        ):
            return 0

        if ro == 0 and co == 0:
            self.max_cherries_collected = max(
                self.max_cherries_collected, cherries_collected_so_far
            )
            return

        cherry_value = grid[ro][co]

        if cherry_value == 1:
            grid[ro][co] = 0
        self.solve2(ro - 1, co, cherries_collected_so_far + cherry_value, grid)
        self.solve2(ro, co - 1, cherries_collected_so_far + cherry_value, grid)
        grid[ro][co] = cherry_value

    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.max_cherries_collected = float("-inf")
        self.solve1(0, 0, 0, grid)
        if self.max_cherries_collected == float("-inf"):
            return 0
        return self.max_cherries_collected


# Recursion
# T.C. -
# S.C  -


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i1, j1, i2, j2, grid):
        # Out of bounds check and thorn check
        if (
            not self.check_in_bounds(i1, j1, len(grid), len(grid[0]))
            or not self.check_in_bounds(i2, j2, len(grid), len(grid[0]))
            or grid[i1][j1] == -1
            or grid[i2][j2] == -1
        ):
            return float("-inf")

        # Base Case

        # If both person1 and person 2 have reach bottom corner
        if (
            i1 == len(grid) - 1
            and j1 == len(grid[0]) - 1
            and i2 == len(grid) - 1
            and j2 == len(grid[0]) - 1
        ):
            return grid[i1][j1]

        # If person1 has reached the bottom corner
        elif (i1 == len(grid) - 1 and j1 == len(grid[0]) - 1) and (
            i2 != len(grid) - 1 and j2 != len(grid[0]) - 1
        ):
            return grid[i1][j1]

        # If person2 has reached the bottom corner
        elif (i2 == len(grid) - 1 and j2 == len(grid[0]) - 1) and (
            i1 != len(grid) - 1 and j1 != len(grid[0]) - 1
        ):
            return grid[i2][j2]

        # Get current cherry count
        c = 0

        if i1 == i2 and j1 == j2:
            c += grid[i1][j1]
        else:
            c += grid[i1][j1] + grid[i2][j2]

        # Hypo
        f1 = self.solve(i1 + 1, j1, i2 + 1, j2, grid)
        f2 = self.solve(i1, j1 + 1, i2, j2 + 1, grid)
        f3 = self.solve(i1 + 1, j1, i2, j2 + 1, grid)
        f4 = self.solve(i1, j1 + 1, i2 + 1, j2, grid)

        # Induction
        return max(f1, f2, f3, f4) + c

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        val = self.solve(0, 0, 0, 0, grid)
        if val == float("-inf"):
            return 0
        return val


# Memoization
# T.C. -
# S.C  -


class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i1, j1, i2, j2, grid, dp):
        # Out of bounds check and thorn check
        if (
            not self.check_in_bounds(i1, j1, len(grid), len(grid[0]))
            or not self.check_in_bounds(i2, j2, len(grid), len(grid[0]))
            or grid[i1][j1] == -1
            or grid[i2][j2] == -1
        ):
            return float("-inf")

        # Cache value

        if (i1, j1, i2, j2) in dp:
            return dp[(i1, j1, i2, j2)]

        # Base Case

        # If both person1 and person 2 have reach bottom corner
        if (
            i1 == len(grid) - 1
            and j1 == len(grid[0]) - 1
            and i2 == len(grid) - 1
            and j2 == len(grid[0]) - 1
        ):
            return grid[i1][j1]

        # If person1 has reached the bottom corner
        elif (i1 == len(grid) - 1 and j1 == len(grid[0]) - 1) and (
            i2 != len(grid) - 1 and j2 != len(grid[0]) - 1
        ):
            return grid[i1][j1]

        # If person2 has reached the bottom corner
        elif (i2 == len(grid) - 1 and j2 == len(grid[0]) - 1) and (
            i1 != len(grid) - 1 and j1 != len(grid[0]) - 1
        ):
            return grid[i2][j2]

        # Get current cherry count
        c = 0

        if i1 == i2 and j1 == j2:
            c += grid[i1][j1]
        else:
            c += grid[i1][j1] + grid[i2][j2]

        # Hypo
        f1 = self.solve(i1 + 1, j1, i2 + 1, j2, grid, dp)
        f2 = self.solve(i1, j1 + 1, i2, j2 + 1, grid, dp)
        f3 = self.solve(i1 + 1, j1, i2, j2 + 1, grid, dp)
        f4 = self.solve(i1, j1 + 1, i2 + 1, j2, grid, dp)

        dp[(i1, j1, i2, j2)] = max(f1, f2, f3, f4) + c

        # Induction
        return dp[(i1, j1, i2, j2)]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}

        val = self.solve(0, 0, 0, 0, grid, dp)
        if val == float("-inf"):
            return 0
        return val


# Tabulation
# T.C. -
# S.C  -

# Space Optimized
# T.C. -
# S.C  -
