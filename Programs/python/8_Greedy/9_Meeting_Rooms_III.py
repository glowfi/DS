# https://leetcode.com/problems/meeting-rooms-iii/ , Hard

# Brute
# T.C. -
# S.C  -

from collections import defaultdict


class Solution:
    def roomWithLowestNumber(self, rooms: dict[int, int], intv: list[list[int]]) -> int:
        for room in rooms:
            pass

        return -1

    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        rooms: dict[int, int] = defaultdict(int)

        for i in range(len(meetings)):
            pass

        return 0


# Optimal
# T.C. -
# S.C  -
