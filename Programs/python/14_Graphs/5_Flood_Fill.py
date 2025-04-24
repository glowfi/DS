# https://leetcode.com/problems/flood-fill/ , Easy

# Optimal [BFS]
# T.C. - O(n)
# S.C  - O(n)

from collections import deque


class Solution:
    def check_in_bounds(self, matrix, ro, co):
        if ro < 0 or co < 0:
            return False
        if ro >= len(matrix) or co >= len(matrix[0]):
            return False
        return True

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        q = deque([[sr, sc]])
        ini_color = image[sr][sc]
        image[sr][sc] = color

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = {}

        while q:
            for i in range(len(q)):
                ro, co = q.popleft()
                for dx, dy in dirs:
                    row, col = ro + dx, co + dy
                    if (
                        self.check_in_bounds(image, row, col)
                        and (row, col) not in seen
                        and image[row][col] == ini_color
                    ):
                        seen[(row, col)] = True
                        image[row][col] = color
                        q.append([row, col])

        return image


# Optimal [DFS]
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def check_in_bounds(self, matrix, ro, co):
        if ro < 0 or co < 0:
            return False
        if ro >= len(matrix) or co >= len(matrix[0]):
            return False
        return True

    def dfs(self, im, seen, r, c, nc, ini):
        if not self.check_in_bounds(im, r, c) or (r, c) in seen or im[r][c] != ini:
            return

        im[r][c] = nc
        seen[(r, c)] = True

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dx, dy in dirs:
            row = r + dx
            col = c + dy
            self.dfs(im, seen, row, col, nc, ini)

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        ini = image[sr][sc]
        r, c = len(image), len(image[0])
        seen = {}
        self.dfs(image, seen, sr, sc, color, ini)
        return image
