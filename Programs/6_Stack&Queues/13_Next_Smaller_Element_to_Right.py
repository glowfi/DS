# https://www.geeksforgeeks.org/problems/help-classmates--141631/1 , Easy

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def help_classmate(self, arr, n):
        out = [-1 for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    out[i] = arr[j]
                    break

        return out


# Optimal
# T.C. - O(n)
# S.C  - O(n)


from collections import deque


class Solution:
    def help_classmate(self, arr, n):
        out = [-1 for _ in range(n)]

        # Take monotonically increasing stack [Bottom-Top increasing Stack storing the right of the array.]
        stk = deque([])

        for i in range(n - 1, -1, -1):
            curr = arr[i]
            while stk and stk[-1] >= curr:
                stk.pop()

            if stk:
                out[i] = stk[-1]
            stk.append(curr)

        return out
