# https://leetcode.com/problems/accounts-merge/description/ , Medium


# Optimal
# T.C. -
# S.C  -


# Algorithm
# + Think about using DSU
# + Every element present in the list should be marked with an unique number.Based on the number of elements present
# we can create a DS of that x number of elements present which now is going to act as nodes
# + We are now going to create a mapping with the email to its node number

from typing import List


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


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        V = len(accounts)
        ds = DisjointSet(V)
        mp = {}

        # Create the (email->node mapping)
        # On finding repitions merge them with the node

        for i in range(V):
            for j in range(1, len(accounts[i])):
                curr_email = accounts[i][j]

                if curr_email not in mp:
                    mp[curr_email] = i
                else:
                    ds.union_by_rank(i, mp[curr_email])

        ans = [[] for _ in range(V)]
        final = []

        for email in mp:
            node = mp[email]
            get_parent_node = ds.getUltimateParent(node)
            ans[get_parent_node].append(email)

        for ind, email in enumerate(ans):
            if len(ans[ind]) > 0:
                ans[ind].sort()
                ans[ind].insert(0, accounts[ind][0])
                final.append(ans[ind])

        return final


# obj = Solution()
# accounts = [
#     ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#     ["John", "johnsmith@mail.com", "john00@mail.com"],
#     ["Mary", "mary@mail.com"],
#     ["John", "johnnybravo@mail.com"],
# ]
# accounts = [
#     ["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
#     ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
#     ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
#     ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
#     ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"],
# ]

# print(obj.accountsMerge(accounts))
