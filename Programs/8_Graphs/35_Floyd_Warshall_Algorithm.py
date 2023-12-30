# https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1 , Medium

# In Floyd Warshall’s algorithm, we need to check every possible path going via each possible node.
# + If there is an edge b/w u and v try to reach v by going via each possible nodes and take the mindistance among them.
# + Create a adjacency matrix and fill all reachable edges with cost and non-reachable edges with infinity.

# Optimal
# T.C. -
# S.C  -


class Solution:
    def shortest_distance(self, matrix):
        # Fix unreachable edges
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == -1:
                    matrix[row][col] = float("inf")
                if row == col:
                    matrix[row][col] = 0

        # Solve
        for node in range(len(matrix)):
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    # mat[u][v] via node k -> mat[u][k]+mat[k][v]
                    currCost = matrix[row][node] + matrix[node][col]
                    matrix[row][col] = min(matrix[row][col], currCost)

        # Fix unreachable edges
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == float("inf"):
                    matrix[row][col] = -1
                if row == col:
                    matrix[row][col] = 0

        return matrix
