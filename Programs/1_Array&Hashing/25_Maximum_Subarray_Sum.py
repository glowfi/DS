# https://leetcode.com/problems/maximum-subarray/,Medium

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float("-inf")

        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                mx = max(sm, mx)
        return mx


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSoFar = float("-inf")

        for i in range(len(nums)):
            currSum += nums[i]

            maxSoFar = max(currSum, maxSoFar)

            if currSum < 0:
                currSum = 0

        return maxSoFar


# Optimal (With array)
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSoFar = float("-inf")
        ansStart, ansEnd = -1, -1

        for i in range(len(nums)):
            if currSum == 0:
                start = i

            currSum += nums[i]

            if currSum > maxSoFar:
                maxSoFar = currSum
                ansStart = start
                ansEnd = i

            if currSum < 0:
                currSum = 0

        print(nums[ansStart : ansEnd + 1])
        return maxSoFar


# Optimal (V2)
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSoFar = float("-inf")

        for i in range(len(nums)):
            currSum += nums[i]
            currSum = max(nums[i], currSum)
            maxSoFar = max(currSum, maxSoFar)

        return maxSoFar
