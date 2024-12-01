# https://leetcode.com/problems/trapping-rain-water/ , Hard


# Better
# T.C. - O(3n)
# S.C  - O(2n)


class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0] * len(height)
        lmax[0] = height[0]
        for i in range(1, len(height)):
            lmax[i] = max(height[i], lmax[i - 1])

        rmax = [0] * len(height)
        rmax[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            rmax[i] = max(height[i], rmax[i + 1])

        trappedWater = 0
        for i in range(1, len(height) - 1):
            trappedWater += min(lmax[i], rmax[i]) - height[i]

        return trappedWater


# Optimal
# T.C. -
# S.C  -
