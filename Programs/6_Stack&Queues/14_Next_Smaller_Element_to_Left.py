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


# Optimal [take monotonically strictly increasing from bottom to top  for R to L iteration storing the right array]
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def leftSmaller(self, n, a):
        nsr = [-1] * n
        stk = []

        for i in range(n):
            while stk and a[stk[-1]] >= a[i]:
                stk.pop(-1)

            if stk:
                nsr[i] = a[stk[-1]]
            else:
                nsr[i] = -1

            stk.append(i)

        return nsr
