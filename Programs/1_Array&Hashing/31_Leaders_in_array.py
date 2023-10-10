# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1,Easy

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def leaders(self, A, N):
        ans = []

        for i in range(len(A)):
            leader = True
            for j in range(i + 1, len(A)):
                if A[i] < A[j]:
                    leader = False
                    break
            if leader:
                ans.append(A[i])
        return ans


# Better
# T.C. -> O(n)+O(n)
# S.C. -> O(n)


class Solution:
    def leaders(self, A, N):
        ans = [A[-1]]
        rmax = [0] * len(A)
        rmax[-1] = A[-1]

        for i in range(len(A) - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], A[i])

        for i in range(len(A) - 2, -1, -1):
            if rmax[i] == A[i]:
                ans.append(A[i])
        ans.reverse()

        return ans


# Optimal
# T.C. -> O(n)+O(n)
# S.C. -> O(1)


class Solution:
    def leaders(self, A, N):
        ans = [A[-1]]
        rmaxSoFar = A[-1]

        for i in range(len(A) - 2, -1, -1):
            if A[i] >= rmaxSoFar:
                ans.append(A[i])
                rmaxSoFar = max(A[i], rmaxSoFar)
        ans.reverse()
        return ans
