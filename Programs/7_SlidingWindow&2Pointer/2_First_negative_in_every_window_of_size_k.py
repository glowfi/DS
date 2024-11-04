# https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1 , Medium

# Brute
# T.C. - O(N-k*k)
# S.C  - O(1)


class Solution:
    def printFirstNegativeInteger(self, arr, k):
        ans = [0] * ((len(arr) - k) + 1)

        for i in range(len(arr) - k + 1):
            for j in range(i, i + k):
                if arr[j] < 0:
                    ans[i] = arr[j]
                    break

        return ans


# Optimal
# T.C. - O(n+n)
# S.C  - O(n)

from collections import deque


class Solution:
    def printFirstNegativeInteger(self, arr, k):
        ans = []
        l, r = 0, -1
        dq = deque([])

        for i in range(k):
            if arr[i] < 0:
                dq.append(i)
            r += 1

        if len(dq) > 0:
            ans.append(arr[dq[0]])
        else:
            ans.append(0)

        while r < len(arr) - 1:
            # Remove calculations
            l += 1
            while dq and dq[0] < l:
                dq.popleft()

            # Do Work
            r += 1
            if arr[r] < 0:
                dq.append(r)

            # Find ans
            if len(dq) > 0:
                ans.append(arr[dq[0]])
            else:
                ans.append(0)

        return ans
