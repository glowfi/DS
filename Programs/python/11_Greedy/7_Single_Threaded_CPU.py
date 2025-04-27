# https://leetcode.com/problems/single-threaded-cpu/ , Medium

# Better
# T.C. - O(nlog(n))+O(nlog(n))
# S.C  - O(m*n*1)

# sort based on enqueu time
# At any given time find out what possible tasks we can process
# select the task with least processing time for time t
# select task with lower index if same processing time

import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted(
            [[task[0], task[1], idx] for idx, task in enumerate(tasks)],
            key=lambda x: x[0],
        )  # sort based on enqueu time

        ans = []
        ready_to_process = []
        i = 0
        time = 0

        while i < len(tasks) or ready_to_process:
            while i < len(tasks) and tasks[i][0] <= time:
                en, pr, idx = tasks[i]
                heapq.heappush(ready_to_process, [pr, idx])
                i += 1

            if not ready_to_process:
                time = tasks[i][
                    0
                ]  # dont just do time+=1 its obvious and move to the time of first task as its sorted
            else:
                pr, idx = heapq.heappop(ready_to_process)
                ans.append(idx)
                time += pr

        return ans


# Optimal
# T.C. -
# S.C  -
