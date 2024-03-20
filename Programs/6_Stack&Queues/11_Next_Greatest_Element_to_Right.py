# https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1 , Easy

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def nextLargerElement(self, arr, n):
        out = [-1 for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    out[i] = arr[j]
                    break

        return out


# Optimal
# T.C. - O(N)
# S.C  - O(N)

from collections import deque


class Solution:
    def nextLargerElement(self, arr, n):
        out = [-1 for _ in range(n)]

        # Take monotonically decreasing stack [Bottom-Top decreasing Stack storing the right of the array.]
        stk = deque([])

        for i in range(n - 1, -1, -1):
            curr = arr[i]
            while stk and stk[-1] <= curr:
                stk.pop()

            if stk:
                out[i] = stk[-1]
            stk.append(curr)

        return out


arr = [16, 17, 4, 3, 5, 2]
arr = [2, 3, 1, 9]
arr = [1, 3, 2, 4]
obj = Solution()
print(obj.nextLargerElement(arr, len(arr)))
