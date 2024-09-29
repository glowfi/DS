# https://www.geeksforgeeks.org/problems/help-classmates--141631/1 , Easy

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def help_classmate(self, arr, n):
        nsr = [-1] * n
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    nsr[i] = arr[j]
                    break
        return nsr


# Optimal [take monotonically strictly increasing from bottom to top  for R to L iteration storing the right array]
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def help_classmate(self, arr, n):
        nsr = [-1] * n
        stk = []

        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop(-1)

            if stk:
                nsr[i] = arr[stk[-1]]
            else:
                nsr[i] = -1

            stk.append(i)

        return nsr
