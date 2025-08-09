# https://leetcode.com/problems/split-array-largest-sum , Hard, BS-on-Ans

# Question
# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.


# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.


# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= k <= min(50, nums.length)

# Brute
# T.C. - O(N*sum(nums))
# S.C  - O(1)

# Intuition
# Do a linear search and the first time you
# see that we are able to split to
# fewer than k a splits we return the current min
# page value


from typing import List


class Solution:
    def isPossible(self, maxSum, arr, k):
        splitsAllocated = 0
        currVal = maxSum

        for val in arr:
            if val <= currVal:
                currVal -= val
            else:
                splitsAllocated += 1
                currVal = maxSum
                currVal -= val

        if currVal >= 0:
            splitsAllocated += 1

        return splitsAllocated <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        st, en = max(nums), sum(nums) + 1

        for i in range(st, en):
            if self.isPossible(i, nums, k):
                return i
        return -1


# Optimal
# T.C. - O(N*log(sum(books)))
# S.C  - O(1)

# Intuition
# Do a binary search if split allocation is possible
# go as left as possible to get min page otherwise
# go right


from typing import List


class Solution:
    def isPossible(self, maxSum, arr, k):
        splitsAllocated = 0
        currVal = maxSum

        for val in arr:
            if val <= currVal:
                currVal -= val
            else:
                splitsAllocated += 1
                currVal = maxSum
                currVal -= val

        if currVal >= 0:
            splitsAllocated += 1

        return splitsAllocated <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        st, en = max(nums), sum(nums)
        minSum = -1

        while st <= en:
            mid = st + (en - st) // 2

            if self.isPossible(mid, nums, k):
                minSum = mid
                en = mid - 1
            else:
                st = mid + 1

        return minSum
