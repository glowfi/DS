# https://leetcode.com/problems/task-scheduler/ , Medium


# Better
# T.C. - O(n)+O(26log26)+O(tlog(26))
# S.C  - O(n)

# Intuition : Pop n+1 elements
# store the n+1 element in a temporary data structure with frequency decremented by 1
# if there are some elements in heap interval+=n+1 or interval+=size of temo data structure
# after then push all the element in the heap only if freq is greater than zero

import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq_map: dict[str, int] = {}
        max_heap = []

        for task in tasks:
            task_freq_map[task] = 1 + task_freq_map.get(task, 0)

        for task_id, freq in task_freq_map.items():
            heapq.heappush(max_heap, [-freq, task_id])  # use -freq for max heap

        time = 0
        while max_heap:
            tmp = []
            for _ in range(n + 1):
                if max_heap:
                    freq, task_id = heapq.heappop(max_heap)
                    tmp.append([freq + 1, task_id])  # decrease freq by 1

            for freq, task_id in tmp:
                if freq < 0:  # if freq is still negative, push back to heap
                    heapq.heappush(max_heap, [freq, task_id])

            time += n + 1 if max_heap else len(tmp)  # update time

        return time
