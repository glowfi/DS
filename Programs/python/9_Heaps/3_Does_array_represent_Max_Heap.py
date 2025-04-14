#  https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1 , Easy


# Better
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def isMaxHeap(self, arr, n):
        def dfs(arr, idx):
            if idx >= n:
                return True

            lcIdx, rcIdx = 2 * idx + 1, 2 * idx + 2

            if lcIdx < n and arr[idx] < arr[lcIdx]:
                return False

            if rcIdx < n and arr[idx] < arr[rcIdx]:
                return False

            return dfs(arr, lcIdx) and dfs(arr, rcIdx)

        return dfs(arr, 0)


# Optimal
# T.C. - O(log(n))
# S.C  - O(1)


class Solution:
    def isMaxHeap(self, arr, n):
        for idx in range(0, n // 2):
            lcIdx = 2 * idx + 1
            if lcIdx < n and arr[idx] < arr[lcIdx]:
                return False

            rcIdx = 2 * idx + 2
            if rcIdx < n and arr[idx] < arr[rcIdx]:
                return False

        return True
