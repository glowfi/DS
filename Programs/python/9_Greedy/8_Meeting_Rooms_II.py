# https://www.geeksforgeeks.org/problems/attend-all-meetings-ii/1 , Medium

# Brute
# T.C. - O(n^2)+O(nlog(n))
# S.C  - O(n)+O(n)


from collections import defaultdict


class Solution:
    def isOverlapping(self, intv1: list[int], intv2: list[int]) -> bool:
        return intv1[-1] > intv2[0] or intv1[0] > intv2[-1]

    def canBeGroupedInExistingGroups(self, intv: list[int], grpMap: dict[int, list]):
        for grpNo in grpMap:
            lastIntervalInCurrentGroup = grpMap[grpNo][-1]
            if not self.isOverlapping(lastIntervalInCurrentGroup, intv):
                grpMap[grpNo].append(intv)
                return True
        return False

    def minMeetingRooms(self, start: list[int], end: list[int]):
        final: list[list[int]] = []

        for i in range(len(start)):
            final.append([start[i], end[i]])

        final.sort(key=lambda x: x[0])
        print(final)

        grps = defaultdict(list[list[int]])
        c = 0
        grps[c].append(final[0])

        for i in range(1, len(final)):
            if not self.canBeGroupedInExistingGroups(final[i], grps):
                c += 1
                grps[c].append(final[i])

        print(grps)

        return len(grps)


# obj = Solution()
# start = [25, 0, 14, 24, 18, 3, 17]
# end = [29, 25, 24, 26, 25, 23, 18]
# start = [2, 9, 6]
# end = [4, 12, 10]
# print(obj.minMeetingRooms(start, end))


# Better
# T.C. - O(nlog(n)) + O(nlog(n))
# S.C  - O(ans)

import heapq


class Solution:
    def minMeetingRooms(self, start, end):
        intervals: list[list[int]] = []

        for i in range(len(start)):
            intervals.append([start[i], end[i]])

        intervals.sort(key=lambda x: x[0])

        heap: list[int] = [intervals[0][-1]]
        heapq.heapify(heap)

        rooms = 1

        for start, end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                rooms += 1
                heapq.heappush(heap, end)

        return rooms


obj = Solution()
start = [25, 0, 14, 24, 18, 3, 17]
end = [29, 25, 24, 26, 25, 23, 18]
# start = [2, 9, 6]
# end = [4, 12, 10]
print(obj.minMeetingRooms(start, end))


# Optimal
# T.C. -
# S.C  -
