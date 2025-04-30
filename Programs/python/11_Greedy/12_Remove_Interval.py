# https://leetcode.com/problems/remove-interval , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(1)

from typing import List


class Solution:

    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:

        # Extracting start and end points of the interval to be removed

        removal_start, removal_end = toBeRemoved

        # This will store the final list of intervals after removing the specified interval

        updated_intervals = []

        # Iterate through each interval in the provided list of intervals

        for interval_start, interval_end in intervals:

            # If the current interval doesn't overlap with the interval to be removed,

            # we can add it to the updated list as-is

            if interval_start >= removal_end or interval_end <= removal_start:

                updated_intervals.append([interval_start, interval_end])

            else:

                # If there is an overlap and the start of the current interval

                # is before the start of the interval to be removed,

                # add the non-overlapping part to the result.

                if interval_start < removal_start:

                    updated_intervals.append([interval_start, removal_start])

                # Similarly, if the end of the current interval is after the end of

                # the interval to be removed, add the non-overlapping part to the result.

                if interval_end > removal_end:

                    updated_intervals.append([removal_end, interval_end])

        # Return the updated list of intervals after removal

        return updated_intervals
