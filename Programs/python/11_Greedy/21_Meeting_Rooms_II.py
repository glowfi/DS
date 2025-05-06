# https://www.geeksforgeeks.org/problems/attend-all-meetings-ii/1 , Medium


# Brute
# T.C. - O(n^2)
# S.C  - O(n)

# Keep on finding whether maximumMeetings that can be conducted in current meeting room
# and rule out meeting time that has been conducted , keep doing until all meeting rooms
# are processed


class Solution:
    def maximumMeetings(self, meeting_times: list[list[int]]):
        meeting_times.sort(key=lambda x: x[1])

        prev_meeting_time = meeting_times[0]
        ans = []

        for i in range(1, len(meeting_times)):
            if prev_meeting_time[-1] <= meeting_times[i][0]:
                prev_meeting_time = meeting_times[i]
            else:
                ans.append([meeting_times[i][0], meeting_times[i][-1]])

        return ans

    def minMeetingRooms(self, start, end):
        meeting_times = []

        for idx, time in enumerate(start):
            meeting_times.append([start[idx], end[idx]])

        meeting_times.sort(key=lambda x: x[0])

        c = 0
        while meeting_times:
            meeting_times = self.maximumMeetings(meeting_times)
            c += 1

        return c


# Brute
# T.C. - O(n^2)
# S.C  - O(n)


# For each meeting room calculate with how many meetings does it overlap
# find out the maximum overlap among them


class Solution:
    def minMeetingRooms(self, start, end):
        meeting_times = []
        for idx, time in enumerate(start):
            meeting_times.append([start[idx], end[idx]])

        max_rooms_required = float("-inf")
        for i in range(len(meeting_times)):
            rooms_required = 1
            for j in range(len(meeting_times)):
                if j == i:
                    continue
                if meeting_times[i][-1] > meeting_times[j][0]:
                    rooms_required += 1
                    max_rooms_required = max(rooms_required, max_rooms_required)

        return max_rooms_required


# Better [Line Sweep]
# T.C. - O(nlog(n))
# S.C  - O(n)

# Intuition
# For each time if its a start time increment one to the specific time
# For each time if its a end time decremtn one to the specific time
# afterwards calulate prefix sum and find the max sum of throughout the iteration


from collections import defaultdict


class Solution:
    def minMeetingRooms(self, start, end):
        time_line = defaultdict(int)
        for st, en in zip(start, end):
            time_line[st] += 1
            time_line[en] -= 1

        min_rooms = 0
        sm = 0
        for i in sorted(time_line.keys()):
            sm += time_line[i]
            min_rooms = max(sm, min_rooms)

        return min_rooms


# Better [Heap]
# T.C. - O(nlog(n))
# S.C  - O(n)

# Intuition
# Use a min heap to track the earliest ending meeting room
# always check if current time overlaps with the earliest endinf meeting
# if its overlaps then we need a new room otherwise we pop the earliest ending meeting
# room
# Assign a new meeting to the room with earliest end time to get optimal results at each step

import heapq


class Solution:
    def minMeetingRooms(self, start, end):
        time_line = []
        for st, en in zip(start, end):
            time_line.append(
                (
                    st,
                    en,
                )
            )

        time_line.sort(key=lambda x: x[0])
        min_heap = [time_line[0][-1]]
        min_rooms = 1
        i = 1

        while i < len(time_line):
            if min_heap[0] > time_line[i][0]:
                min_rooms += 1
                heapq.heappush(min_heap, time_line[i][-1])
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, time_line[i][-1])
            i += 1

        return min_rooms


# Optimal [Two pointer]
# T.C. - O(nlog(n))
# S.C  - O(1)

# Intuition
# fix i pointer in start and j pointer in end
# see which time is lesser
# if i is lesser increment i and add 1 to counter
# if j is lesser increment j and decrement 1 to counter
# keep track of the max counter throughout the iteration
# counter signifies no of platforms


class Solution:
    def minMeetingRooms(self, start, end):
        c = 0
        min_rooms = 0
        start.sort()
        end.sort()

        i, j = 0, 0

        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                i += 1
                c += 1
            else:
                j += 1
                c -= 1
            min_rooms = max(min_rooms, c)

        return min_rooms
