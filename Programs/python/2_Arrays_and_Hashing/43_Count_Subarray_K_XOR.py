# https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/0, Medium, SubarrayXORCount

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
# T.C. - O(N^2)
# S.C  - O(N)

# Intuition
# Generate all subarrays
# count subarrays with k xor from them


class Solution:
    def subarrayXor(self, arr: list[int], k: int) -> int:
        c = 0

        for i in range(len(arr)):
            xor = 0
            for j in range(i, len(arr)):
                xor ^= arr[j]

                if xor == k:
                    c += 1

        return c


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# Now, there may exist multiple subarrays with the prefix xor pref^k. So, the number of subarrays
# with xor k that we can generate from the entire subarray ending at index i, is exactly equal
# to the number of subarrays with the prefix xor pref^k, that we can remove from the entire subarray.


class Solution:
    def subarrayXor(self, arr: list[int], k: int) -> int:
        pref_xor = 0
        count = 0
        xor_mp = {0: 1}

        for i in range(len(arr)):
            pref_xor ^= arr[i]

            diff_xor = pref_xor ^ k

            if diff_xor in xor_mp:
                count += xor_mp[diff_xor]

            if pref_xor in xor_mp:
                xor_mp[pref_xor] += 1
            else:
                xor_mp[pref_xor] = 1

        return count
