# https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1, Medium, Prefix XOR + HashMap

# Question
# Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

# Examples:

# Input: arr[] = [4, 2, 2, 6, 4], k = 6
# Output: 4
# Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.

# Input: arr[] = [5, 6, 7, 8, 9], k = 5
# Output: 2
# Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.

# Input: arr[] = [1, 1, 1, 1], k = 0
# Output: 4
# Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1].

# Constraints:
# 1 ≤ arr.size() ≤ 10^5
# 0 ≤ arr[i] ≤10^5
# 0 ≤ k ≤ 10^5

# Brute
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# Generate all possible subarrays and check which subarrays
# gives us xor k

from typing import List


def countSubarraysXor_bruteforce(arr: List[int], k: int):
    cnt = 0
    n = len(arr)
    for i in range(n):
        cur_xor = 0
        for j in range(i, n):
            cur_xor ^= arr[j]
            if cur_xor == k:
                cnt += 1
    return cnt


# Optimal
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# We are going to use the concept of prefix XOR.
# Observe that if a subarray ending at index i has XOR equal to k,
# then the XOR of the part of the array before that subarray must be x ⊕ k, where x is the current prefix XOR up to i.
# For a subarray that ends at i with prefix XOR x, removing
# the earlier segment whose prefix XOR is x ⊕ k leaves exactly the segment whose XOR is k.
# There can be many earlier positions whose prefix XOR equals x ⊕ k.
# The number of subarrays with XOR k that end at i is therefore exactly the number of times the value x ⊕ k has already been seen.
# We keep a running prefix XOR x while scanning the array, and at each index i
# we check whether the value x ⊕ k has been encountered before. Every
# prior occurrence of x ⊕ k indicates a distinct subarray ending at i whose XOR is k.


from typing import List


class Solution:
    def subarrayXor(self, arr: List[int], k: int):
        curr_pref_xor = 0
        freq_mp = {0: 1}
        c = 0

        for _, num in enumerate(arr):
            curr_pref_xor ^= num
            complement = curr_pref_xor ^ k

            if complement in freq_mp:
                c += freq_mp[complement]

            freq_mp[curr_pref_xor] = 1 + freq_mp.get(curr_pref_xor, 0)

        return c
