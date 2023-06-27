# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/ , Medium

# Brute
# T.C. -> O(max(nums)*n)
# S.C. -> O(1)

import math


class Solution:
    def getSum(self, arr, x):
        s = 0
        for i in arr:
            s += math.ceil(i / x)
        return s

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for i in range(1, max(nums) + 1):
            k = self.getSum(nums, i)
            if k <= threshold:
                return i


# Optimal
# T.C. -> O(log(max(n))*n)
# S.C. -> O(1)

import math


class Solution:
    def getSum(self, arr, x):
        s = 0
        for i in arr:
            s += math.ceil(i / x)
        return s

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        st, en = 1, max(nums)

        while st <= en:
            mid = (st + en) // 2

            if self.getSum(nums, mid) <= threshold:
                en = mid - 1
            else:
                st = mid + 1
        return st
