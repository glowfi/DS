# https://leetcode.com/problems/pascals-triangle/,Easy

# Given R and C Tell me element at that place


# R-1
#    C
#      C-1


# T.C -> O(r)
# S.C -> O(1)


def findncr(n, r):
    ans = 1
    for i in range(r):
        ans *= (n - i) // (i + 1)

    return ans


# Print any Nth Row of pascals triangle ,given

# T.C -> O(N)
# S.C -> O(N)


def printRow(N):
    ans = 1
    ls = []

    ls.append(1)
    for i in range(1, N):
        ans *= N - i
        ans //= i
        ls.append(ans)

    return ls


# Print pascals triangle for given N rows

# T.C -> O(N^2)
# T.C -> O(N)


class Solution:
    def printRow(self, N):
        ans = 1
        ls = []

        ls.append(1)
        for i in range(1, N):
            ans *= N - i
            ans //= i
            ls.append(ans)

        return ls

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(1, numRows + 1):
            ans.append(self.printRow(i))

        return ans
