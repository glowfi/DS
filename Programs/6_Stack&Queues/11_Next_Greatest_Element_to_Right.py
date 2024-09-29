# https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1 , Easy

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def nextLargerElement(self, arr, n):
        ngr = [-1 for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    ngr[i] = arr[j]
                    break

        return ngr


# Optimal [take monotonically strictly decreasing from bottom to top  for R to L iteration storing the right array]
# T.C. - O(N)
# S.C  - O(N)


class Solution:
    def nextLargerElement(self, arr, n):
        ngr = [-1 for _ in range(n)]
        stk = []

        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop(-1)

            if stk:
                ngr[i] = arr[stk[-1]]
            else:
                ngr[i] = -1

            stk.append(i)

        return ngr


arr = [16, 17, 4, 3, 5, 2]
arr = [2, 3, 1, 9]
arr = [1, 3, 2, 4]
obj = Solution()
print(obj.nextLargerElement(arr, len(arr)))
