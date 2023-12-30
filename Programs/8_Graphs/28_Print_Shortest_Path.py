# NA , Medium


# Optimal
# T.C. - O(Elog(V))+O(Lenght_of_shortest_path)
# S.C  - O(E)+O(V)+O(V)

from math import prod
from sortedcontainers import SortedSet


class Solution:
    def dijkstra(self, V, adj, S):
        st = SortedSet([(0, S)])
        dist = [float("inf") for _ in range(V)]
        dist[S] = 0
        parent_path = {0: -1}

        while st:
            for _ in range(len(st)):
                d, node = st[0]
                st.discard((d, node))

                for neighbour, wt in adj[node]:
                    if d + wt < dist[neighbour]:
                        if (
                            dist[neighbour] != float("inf")
                            and (dist[neighbour], neighbour) in st
                        ):
                            st.discard((dist[neighbour], neighbour))
                        dist[neighbour] = d + wt
                        st.add((d + wt, neighbour))
                        parent_path[neighbour] = node

        start = V - 1
        path = [start]

        while True:
            if start == 0:
                break

            start = parent_path[start]
            path.append(start)

        return path[::-1]


V = 5
adj = {
    0: [(3, 1), (1, 2)],
    1: [(0, 2), (2, 4), (4, 5)],
    2: [(3, 3), (1, 4), (4, 1)],
    3: [(0, 1), (2, 3)],
    4: [(1, 5), (2, 1)],
}
S = 0
obj = Solution()
print(obj.dijkstra(V, adj, S))
