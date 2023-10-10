# https://practice.geeksforgeeks.org/problems/who-will-win-1587115621/1,Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def searchInSorted(self, arr, N, K):
        found = -1
        for i in range(len(arr)):
            if arr[i] == K:
                found = 1
                break

        return found
