# https://www.geeksforgeeks.org/problems/attend-all-meetings/1 , Easy

# Optimal
# T.C. - O(nlog(n))+O(n)
# S.C  - O(1)


class Solution:
    def canAttend(self, arr):
        arr.sort(key=lambda x: x[0])

        prev_end = arr[0][-1]
        for start, end in arr[1:]:
            if start < prev_end:
                return False
            else:
                prev_end = end
        return True
