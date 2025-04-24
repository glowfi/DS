# https://www.geeksforgeeks.org/problems/maximum-sum-combination/0 , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(1)


class Solution:
    def maxCombinations(self, N, K, A, B):
        res = []
        for i in range(N):
            curr_elem = A[i]
            for j in range(N):
                res.append(B[j] + curr_elem)

        return sorted(res, reverse=True)[:K]


# Optimal
# T.C. - O()
# S.C  - O()


class Solution:
    def maxCombinations(self, N, K, A, B):
        pass
