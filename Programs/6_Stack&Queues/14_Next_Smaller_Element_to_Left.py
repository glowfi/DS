# https://www.geeksforgeeks.org/problems/smallest-number-on-left3403/1 , Easy


# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def leftSmaller(self, n, a):
        out = [-1 for _ in range(n)]

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if a[j] < a[i]:
                    out[i] = a[j]
                    break

        return out


# Optimal
# T.C. - O(n)
# S.C  - O(n)


from collections import deque


class Solution:
    def leftSmaller(self, n, a):
        out = [-1 for _ in range(n)]

        # Take monotonically increasing stack [Bottom-Top increasing Stack storing the left of the array.]
        stk = deque([])

        for i in range(n):
            curr = a[i]
            while stk and stk[-1] >= curr:
                stk.pop()

            if stk:
                out[i] = stk[-1]
            stk.append(curr)

        return out
