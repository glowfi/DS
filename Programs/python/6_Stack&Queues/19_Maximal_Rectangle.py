# https://leetcode.com/problems/maximal-rectangle/ , Hard


# Better
# T.C. -
# S.C  -


class Solution:
    def MAH(self, arr):
        nsl = [-1 for _ in range(len(arr))]
        nsr = [len(arr)] * len(arr)

        # Make the nsl array
        stk = []
        for i in range(len(arr)):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop(-1)

            if stk:
                nsl[i] = stk[-1]
            else:
                nsl[i] = -1

            stk.append(i)

        # Make the nsr array
        stk = []
        for i in range(len(arr) - 1, -1, -1):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop(-1)

            if stk:
                nsr[i] = stk[-1]
            else:
                nsr[i] = len(arr)

            stk.append(i)

        maxArea = float("-inf")
        for i in range(len(arr)):
            currArea = (nsr[i] - nsl[i] - 1) * arr[i]
            maxArea = max(maxArea, currArea)

        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = float("-inf")

        tmpArr = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    tmpArr[j] = 0
                else:
                    tmpArr[j] += int(matrix[i][j])
            maxArea = max(maxArea, self.MAH(tmpArr))

        return maxArea


# Optimal
# T.C. -
# S.C  -


class Solution:
    def MAH(self, arr):
        pass

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = float("-inf")

        tmpArr = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    tmpArr[j] = 0
                else:
                    tmpArr[j] += int(matrix[i][j])
            maxArea = max(maxArea, self.MAH(tmpArr))

        return maxArea
