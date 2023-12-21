# https://www.geeksforgeeks.org/problems/alien-dictionary/1 , Hard

# Optimal
# T.C. - O(len_of_words_in_list)+O(N)+O(N)
# S.C  - O(N)+O(N)+O(N)+O(N)


from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, alien_dict, N, K):
        adj = defaultdict(list)
        cmap = {}
        _cmap = {}
        idx = 97

        for i in range(K):
            cmap[chr(idx)] = i
            _cmap[i] = chr(idx)
            idx += 1

        for i in range(len(alien_dict) - 1):
            word1, word2 = alien_dict[i], alien_dict[i + 1]
            stop = min(len(word1), len(word2))
            i = 0
            while i < stop:
                if word1[i] != word2[i]:
                    adj[cmap[word1[i]]].append(cmap[word2[i]])
                    break
                i += 1

        V = K

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

        if len(ans) == K:
            for i in range(len(ans)):
                ans[i] = _cmap[ans[i]]
            return ans
        return []
