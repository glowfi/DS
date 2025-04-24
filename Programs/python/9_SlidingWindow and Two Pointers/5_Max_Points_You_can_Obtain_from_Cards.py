# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/ , Medium


# Brute
# T.C. - O(N^2)
# S.C  - O(1)


from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        mxScore = float("-inf")

        front, back = k, 0

        for _ in range(k + 1):
            fromFrontSum = sum(cardPoints[:front])
            fromBackSum = sum(cardPoints[::-1][:back])

            mxScore = max(fromFrontSum + fromBackSum, mxScore)

            front -= 1
            back += 1

        return mxScore


# Better
# T.C. - O(N+N)
# S.C  - O(N+N)


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l, r = k - 1, n

        LpreFixSum = [0] * n
        RpreFixSum = [0] * n
        sm1, sm2 = 0, 0
        for i in range(len(cardPoints)):
            sm1 += cardPoints[i]
            LpreFixSum[i] = sm1

            sm2 += cardPoints[len(cardPoints) - i - 1]
            RpreFixSum[n - i - 1] = sm2

        # print(LpreFixSum, RpreFixSum)

        mxSm = float("-inf")

        for i in range(k + 1):
            sm1, sm2 = (LpreFixSum[l] if l >= 0 else 0), (
                RpreFixSum[r] if r <= n - 1 else 0
            )

            # print(sm1, sm2)

            mxSm = max(mxSm, sm1 + sm2)

            l -= 1
            r -= 1

        return mxSm


# Optimal
# T.C. - O(N)
# S.C  - O(1)


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = k - 1
        r = len(cardPoints)

        mxScore = float("-inf")
        score = 0
        for i in range(k):
            score += cardPoints[i]
        mxScore = max(score, mxScore)

        for i in range(k):
            score -= cardPoints[l]
            l -= 1

            r -= 1
            score += cardPoints[r]

            mxScore = max(mxScore, score)

        return mxScore


obj = Solution()
cardPoints = [1, 2, 3, 4, 5, 6, 1]
cardPoints = [100, 40, 17, 9, 73, 75]
k = 3

print(obj.maxScore(cardPoints, k))
