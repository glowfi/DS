# https://practice.geeksforgeeks.org/problems/number-of-provinces/1 , Medium


# Optimal
# T.C. - O(n^2*4*alpha)+O(n)
# S.C  - O(n^2)+O(n)+O(n)


class DisjointSet:
    def __init__(self, V):
        self.rank = [0 for _ in range(V + 1)]
        self.size = [1 for _ in range(V + 1)]
        self.parent = [i for i in range(V + 1)]

    def getUltimateParent(self, node):
        """
        Keep doing path compression as u backtrack which is to keep pointed the nodes to ultimate_parent
        """
        if self.parent[node] == node:
            return node

        parent = self.getUltimateParent(self.parent[node])
        # Path compression
        self.parent[node] = parent
        return parent

    def union_by_rank(self, u, v):
        """
        + Get ultimate parent of u and v
        + Determinte the rank of ultimate parent of u and v
        + Connect the smaller rank to larger rank ultimate parent node
        + Only increase rank if found equal rank nodes
        """

        # Get parent
        up_u = self.getUltimateParent(u)
        up_v = self.getUltimateParent(v)

        # return if equal parent
        if up_u == up_v:
            return

        # Get rank
        rank_u = self.rank[u]
        rank_v = self.rank[v]

        if rank_u > rank_v:
            self.parent[up_v] = up_u

        elif rank_v > rank_u:
            self.parent[up_u] = up_v

        else:
            self.rank[u] += 1
            self.parent[up_v] = up_u


class Solution:
    def numProvinces(self, adj, V):
        c = 0

        ds = DisjointSet(V)

        for i in range(len(adj)):
            for j in range(len(adj[0])):
                if adj[i][j] == 1:
                    ds.union_by_rank(i, j)
                    ds.union_by_rank(j, i)

        for i in range(V):
            if ds.getUltimateParent(i) == i:
                c += 1

        return c
