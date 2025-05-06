# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1 , Medium


# Optimal
# T.C. - O(nlog(n))
# S.C  - O(1)


class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        c = 0
        min_rooms = 0
        arr.sort()
        dep.sort()

        i, j = 0, 0

        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                i += 1
                c += 1
            else:
                j += 1
                c -= 1
            min_rooms = max(min_rooms, c)

        return min_rooms
