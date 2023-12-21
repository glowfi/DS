# https://practice.geeksforgeeks.org/problems/topological-sort/1 , Medium

# Defination
# Linear ordering of vertices such that if there is
# an edge b/w u and v u appears before v in that
# Linear ordering

# Algorithm
# + Works only for DAG. Will get orderings of unsual length if DAG not used
# + Traverse the graph component wise
# + Take a visted array and only visit a node if not visted
# + DAG's all component will have atlest one node with indeegree
# zero so atleast one node from each  component will be pushed
# in the queue so we do not need visited array
# + Find indegree of all nodes
# + Insert the nodes with indegree zero to the queue as they can be placed at first as they do not have incoming edges
# + Keep popping from front of the queue and decrease the indeegree value of its neighbour nodes
# + if indeegree value equals 0 append them to queue

# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)

from collections import deque


class Solution:
    def topoSort(self, V, adj):
        indeg = [0 for _ in range(V)]

        for i in range(V):
            for j in adj[i]:
                indeg[j] += 1

        q = deque([])
        ans = []

        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                # Node in topoSort so remove indeegrees of neighbouring nodes
                ans.append(node)

                for neighbour in adj[node]:
                    indeg[neighbour] -= 1

                    if indeg[neighbour] == 0:
                        q.append(neighbour)

        return ans
