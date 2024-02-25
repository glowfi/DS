# https://leetcode.com/problems/longest-string-chain/ , Medium


# Memoization
# T.C. - O(nlog(n))+O(n*avg(words))
# S.C  - O(n^2)+O(n)


class Solution:
    def check_predecessor(self, w1, w2):
        if len(w2) != len(w1) + 1:
            return False
        i, j = 0, 0
        while j < len(w2):
            if i < len(w1) and w1[i] == w2[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(w1) and j == len(w2)

    def solve(self, currIdx, prevIdx, words, dp):
        if currIdx == len(words):
            return 0

        if dp[currIdx][prevIdx + 1] != -1:
            return dp[currIdx][prevIdx + 1]

        take = 0
        if prevIdx == -1 or self.check_predecessor(words[prevIdx], words[currIdx]):
            take = 1 + self.solve(currIdx + 1, currIdx, words, dp)
        notTake = 0 + self.solve(currIdx + 1, prevIdx, words, dp)

        dp[currIdx][prevIdx + 1] = max(take, notTake)

        return dp[currIdx][prevIdx + 1]

    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        dp = [[-1 for _ in range(len(words) + 1)] for _ in range(len(words) + 1)]
        return self.solve(0, -1, words, dp)
