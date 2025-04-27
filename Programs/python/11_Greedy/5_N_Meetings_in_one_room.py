# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1 , Easy

# Optimal
# T.C. - O(nlog(n))+O(n)
# S.C  - O(start*end)

# Selection criteria : select the meetings which will end first


class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, start, end):
        meeting_times = []

        for idx, time in enumerate(start):
            meeting_times.append([start[idx], end[idx]])

        meeting_times.sort(key=lambda x: x[1])

        i = 0
        prev_meeting_time = meeting_times[0]
        meetings_count = 1

        for i in range(1, len(meeting_times)):
            if prev_meeting_time[-1] < meeting_times[i][0]:
                meetings_count += 1
                prev_meeting_time = meeting_times[i]

        return meetings_count
