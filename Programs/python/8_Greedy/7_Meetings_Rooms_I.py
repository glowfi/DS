# https://www.geeksforgeeks.org/problems/attend-all-meetings/1 , Easy

# Optimal
# T.C. - O(nlog(n))+O(n)
# S.C  - O(1)


class Solution:
    def canAttend(self, arr: list[list[int]]):
        arr.sort(key=lambda x: x[0])

        for i in range(1, len(arr)):
            prev_interval = arr[i - 1]
            curr_interval = arr[i]

            if (
                prev_interval[-1] > curr_interval[0]
                or prev_interval[0] > curr_interval[-1]
            ):
                return False

        return True
