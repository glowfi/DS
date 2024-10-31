# https://leetcode.com/problems/largest-rectangle-in-histogram/ , Hard


# Better
# T.C. - O(n)+O(n)+O(n)
# S.C  - O(n)+O(n)+O(n)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        nsl = [-1 for _ in range(len(heights))]
        nsr = [len(heights)] * len(heights)

        # Make the nsl array
        stk = []
        for i in range(len(heights)):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop(-1)

            if stk:
                nsl[i] = stk[-1]
            else:
                nsl[i] = -1

            stk.append(i)

        # Make the nsr array
        stk = []
        for i in range(len(heights) - 1, -1, -1):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop(-1)

            if stk:
                nsr[i] = stk[-1]
            else:
                nsr[i] = len(heights)

            stk.append(i)

        maxArea = float("-inf")
        for i in range(len(heights)):
            currArea = (nsr[i] - nsl[i] - 1) * heights[i]
            maxArea = max(maxArea, currArea)

        return maxArea


# Optimal
# T.C. -
# S.C  -


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass
