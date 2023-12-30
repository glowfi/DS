# https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1 , Medium


# Optimal
# T.C. - Elog(V)
# S.C  - O(E)+O(V)

# Erase already explored paths if we have found some better distance

from sortedcontainers import SortedSet


class Solution:
    def dijkstra(self, V, adj, S):
        st = SortedSet([(0, S)])
        dist = [float("inf") for _ in range(V)]
        dist[S] = 0

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

        return dist


V = 3
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
S = 2
obj = Solution()
print(obj.dijkstra(V, adj, S))
