# https://www.geeksforgeeks.org/problems/the-celebrity-problem/1 , Medium

# Brute
# T.C. - O(n^2)+O(n)
# S.C  - O(2n)


class Solution:
    def celebrity(self, mat):
        incoming = [0] * len(mat)
        outgoing = [0] * len(mat)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    outgoing[i] += 1
                    incoming[j] += 1

        for i in range(len(incoming)):
            if incoming[i] == len(mat) - 1 and outgoing[i] == 0:
                return i

        return -1


# Optimal
# T.C. -
# S.C  -


class Solution:
    def celebrity(self, mat):
        pass
