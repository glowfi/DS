# https://leetcode.com/problems/maximum-length-of-pair-chain/ , Medium

# Memoization
# T.C. - O(n)+O(nlog(n))
# S.C  - O(n^2)+O(n)


class Solution:
    def solve(self, currIdx, prevIdx, pairs, dp):
        if currIdx == len(pairs):
            return 0

        if dp[currIdx][prevIdx + 1] != -1:
            return dp[currIdx][prevIdx + 1]

        take = 0

        pair2 = pairs[currIdx]
        pair1 = pairs[prevIdx]

        if prevIdx == -1 or pair2[0] > pair1[1]:
            take = 1 + self.solve(currIdx + 1, currIdx, pairs, dp)
        notTake = 0 + self.solve(currIdx + 1, prevIdx, pairs, dp)

        dp[currIdx][prevIdx + 1] = max(take, notTake)

        return dp[currIdx][prevIdx + 1]

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [[-1 for _ in range(len(pairs) + 1)] for _ in range(len(pairs) + 1)]
        return self.solve(0, -1, pairs, dp)


# Space Optimized
# T.C. - O(n^2)+O(nlog(n))
# S.C  - O(n)+O(n)


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [0 for _ in range(len(pairs) + 1)]
        tmp = [0 for _ in range(len(pairs) + 1)]

        for currIdx in range(len(pairs), -1, -1):
            for prevIdx in range(currIdx - 1, -2, -1):
                if currIdx == len(pairs):
                    tmp[prevIdx + 1] = 0
                else:
                    pair2 = pairs[currIdx]
                    pair1 = pairs[prevIdx]

                    take = 0

                    if prevIdx == -1 or pair2[0] > pair1[1]:
                        take = 1 + dp[currIdx + 1]
                    notTake = 0 + dp[prevIdx + 1]

                    tmp[prevIdx + 1] = max(take, notTake)
            dp = tmp

        return dp[-1 + 1]
