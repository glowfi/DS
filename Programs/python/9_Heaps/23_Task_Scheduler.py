# https://leetcode.com/problems/task-scheduler/ , Medium


# Better
# T.C. - O(n)+O(26log26)+O(tlog(26))
# S.C  -

# Intuition : Pop n+1 elements

import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        max_heap = []

        for task in tasks:
            freq_map[task] = 1 + freq_map.get(task, 0)

        for _, freq in freq_map.items():
            heapq.heappush(max_heap, freq * -1)

        interval = 0

        while max_heap:
            tmp = []
            for _ in range(n + 1):
                if len(max_heap) > 0:
                    freq = heapq.heappop(max_heap)
                    tmp.append(freq + 1)

            for f in tmp:
                if f != 0:
                    heapq.heappush(max_heap, f)

            if len(max_heap) == 0:
                interval += len(tmp)
            else:
                interval += n + 1

        return interval
