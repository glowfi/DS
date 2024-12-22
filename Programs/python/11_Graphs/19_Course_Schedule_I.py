# https://leetcode.com/problems/course-schedule/ , Medium


# Optimal
# T.C. - O(n)+O(n)
# S.C  - O(n)+O(n)

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)

        V = numCourses

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

        for i in range(len(indeg)):
            if indeg[i] != 0:
                return False
        return True
