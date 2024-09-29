# NA , Easy

# Brute
# T.C. - O(N^2)
# S.C  - O(1)


class Solution:
    def nextGreatestElementToLeft(self, arr, n):
        ngl = [-1] * n

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if arr[j] > arr[i]:
                    ngl[i] = arr[j]
                    break
        return ngl


# Optimal [take monotonically strictly decreasing from bottom to top  for L to R iteration storing the left array]
# T.C. - O(N)
# S.C  - O(N)


class Solution:
    def nextGreatestElementToLeft(self, arr, n):
        ngl = [-1] * n
        stk = []

        for i in range(n):
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop(-1)

            if stk:
                ngl[i] = arr[stk[-1]]
            else:
                ngl[i] = -1

            stk.append(i)

        return ngl


arr = [16, 17, 4, 3, 5, 2]
arr = [2, 3, 1, 9]
arr = [1, 3, 2, 4]
arr = [10, 4, 2, 20, 40, 12, 30]
obj = Solution()
print(obj.nextGreatestElementToLeft(arr, len(arr)))
