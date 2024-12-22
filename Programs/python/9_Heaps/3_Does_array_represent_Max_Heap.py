#  https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1 , Easy


# Better
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def isMaxHeap(self, arr, n):
        def dfs(i):
            if i >= n:
                return True
            lcIdx, rcIdx = (2 * i) + 1, (2 * i) + 2
            if lcIdx < n and arr[i] < arr[lcIdx]:
                return False
            if rcIdx < n and arr[i] < arr[rcIdx]:
                return False

            return dfs(lcIdx) and dfs(rcIdx)

        return dfs(0)


# Optimal
# T.C. - O(log(n))
# S.C  - O(1)


class Solution:
    def isMaxHeap(self, arr, n):
        for i in range(n // 2):
            lcIdx, rcIdx = (2 * i) + 1, (2 * i) + 2

            if lcIdx < n and arr[i] < arr[lcIdx]:
                return False
            if rcIdx < n and arr[i] < arr[rcIdx]:
                return False

        return True
