# https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1 , Medium


# Optimal
# T.C. - O(V*E)
# S.C  - O(V)


class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    """
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    """

    def relax(self, dist, edge_list):
        for edge in edge_list:
            u, v, wt = edge
            if dist[u] != 10**8:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

    def bellman_ford(self, V, edges, S):
        dist = [10**8 for _ in range(V)]
        dist[S] = 0

        for i in range(V - 1):
            self.relax(dist, edges)

        # Cycle if after Nth iteration dist array gets updated
        for edge in edges:
            u, v, wt = edge
            if dist[u] != 10**8:
                if dist[u] + wt < dist[v]:
                    return [-1]

        # No negative cycle
        return dist


# obj = Solution()
# E = [[0, 1, 5], [1, 0, 3], [1, 2, -1], [2, 0, 1]]
# S = 2
# V = 3
# print(obj.bellman_ford(V, E, S))
