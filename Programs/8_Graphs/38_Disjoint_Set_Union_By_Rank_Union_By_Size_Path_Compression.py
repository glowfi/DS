# NA , Medium


# Optimal
# T.C. - O(4alpha)
# S.C  - O(n)+O(n)


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

    def union_by_size(self, u, v):
        """
        + Get ultimate parent of u and v
        + Determinte the size of ultimate parent of u and v
        + Connect the smaller size to larger size ultimate parent node
        + Only increase size if found equal size nodes
        """

        # Get parent
        up_u = self.getUltimateParent(u)
        up_v = self.getUltimateParent(v)

        # return if equal parent
        if up_u == up_v:
            return

        # Get size
        size_u = self.size[u]
        size_v = self.size[v]

        if size_u > size_v:
            self.parent[v] = u
            self.size[u] += self.size[v]
        else:
            self.parent[u] = v
            self.size[v] += self.size[u]


obj = DisjointSet(7)

obj.union_by_rank(1, 2)
obj.union_by_rank(2, 3)
obj.union_by_rank(4, 5)
obj.union_by_rank(6, 7)
obj.union_by_rank(5, 6)
obj.union_by_rank(3, 7)


obj.union_by_size(1, 2)
obj.union_by_size(2, 3)
obj.union_by_size(4, 5)
obj.union_by_size(6, 7)
obj.union_by_size(5, 6)
obj.union_by_size(3, 7)
