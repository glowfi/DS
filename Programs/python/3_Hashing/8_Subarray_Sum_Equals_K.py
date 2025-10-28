# https://leetcode.com/problems/subarray-sum-equals-k, Medium, Prefix Sum + HashMap

# Question
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2


# Constraints:

# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7

# Brute
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# Generate all possible subarrays and check which subarrays
# gives us sum k

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0

        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]

                if sm == k:
                    c += 1

        return c


# Optimal
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# We are going to use the concept of prefix sum.
# we need to observe that if there exists another
# subarray ending at index i with sum k,
# then the prefix sum of the rest of the subarray will be x-k.
# for a subarray ending at index i with the prefix sum x,
# if we remove the part with the prefix sum x-k, we will
# be left with the part whose sum is equal to k.
# Now, there may exist multiple subarrays with the prefix sum x-k.
# So, the number of subarrays with sum k that we can generate
# from the entire subarray ending at index i, is exactly equal
# to the number of subarrays with the prefix sum x-k,
# that we can remove from the entire subarray.
# We carry the cumultaive sum(x) till now and at
# every index i we are going to check if there
# exists a sum (x-k) we have encounterd before.
# if we have encounterd (x-k) then we can say
# there exists a subarray of size k.

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_pref_sum = 0
        freq_mp = {0: 1}
        c = 0

        for num in nums:
            curr_pref_sum += num
            complement = curr_pref_sum - k

            if complement in freq_mp:
                c += freq_mp[complement]

            freq_mp[curr_pref_sum] = freq_mp.get(curr_pref_sum, 0) + 1

        return c
