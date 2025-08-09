# <Question Link> , Medium, LongestSubarraySum

# Question

# Given an array arr[] and a positive integer k, find the length of the longest subarray with the sum of the elements divisible by k.
# Note: If there is no subarray with sum divisible by k, then return 0.

# Examples :

# Input: arr[] = [2, 7, 6, 1, 4, 5], k = 3
# Output: 4
# Explanation: The subarray [7, 6, 1, 4] has sum = 18, which is divisible by 3.

# Input: arr[] = [-2, 2, -5, 12, -11, -1, 7], k = 3
# Output: 5
# Explanation: The subarray [2, -5, 12, -11, -1] has sum = -3, which is divisible by 3.

# Input: arr[] = [1, 2, -2], k = 2
# Output: 2
# Explanation: The subarray is [2, -2] has sum = 0, which is divisible by 2.

# Constraints:
# 1 <= arr.size() <= 10^6
# 1 <= k <= 10^6
# -10^6 <= arr[i] <= 10^6

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# generate all subarrays
# among them find the longest subarray divisible by k


class Solution:
    def longestSubarrayDivK(self, arr: list[int], k: int) -> int:
        mx_len = 0

        for i in range(len(arr)):
            sm = 0
            for j in range(i, len(arr)):
                sm += arr[j]
                if sm % k == 0:
                    mx_len = max(mx_len, j - i + 1)

        return mx_len


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


class Solution:
    def longestSubarrayDivK(self, arr: list[int], k: int) -> int:
        mx_len = 0
        sm = 0
        remainder_map = {0: -1}

        for i in range(len(arr)):
            sm += arr[i]

            rem = sm % k

            if rem < 0:  # dont store negative remainder
                rem += k

            if rem in remainder_map:
                mx_len = max(mx_len, i - remainder_map[rem])

            if rem not in remainder_map:
                remainder_map[rem] = i

        return mx_len
