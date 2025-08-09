# https://leetcode.com/problems/subarray-sums-divisible-by-k , Medium, SubarraySumCount

# Question
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.


# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0


# Constraints:

# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# 2 <= k <= 10^4


# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Generate all subarrays
# from those subarrays count subarray sum divisible
# by k

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                if sm % k == 0:
                    count += 1

        return count


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition

# suppose i have a below array:
# ------- S1(x)      sum1 with x remainder
# a b c d e f g h i j k l
# ------------------- S2(x)  sum2 with x remainder

# it can be mathematically proven s2-s1 is divisible by k
# s1= kn1+x
# s2= kn2+x
# s1-s2=k(n1-n2) # divisible
# keep storing remainder for correspdoing prefix sum
# check if we have seen this remainder before


from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        rem_count_mp = {0: 1}
        sm = 0

        for i in range(len(nums)):
            sm += nums[i]
            rem = sm % k

            if rem < 0:
                rem += k

            if rem in rem_count_mp:
                count += rem_count_mp[rem]

            if rem not in rem_count_mp:
                rem_count_mp[rem] = 1
            else:
                rem_count_mp[rem] += 1

        return count
