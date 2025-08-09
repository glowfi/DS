# https://leetcode.com/problems/kth-missing-positive-number , Easy, BS-on-Ans

# Question
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.


# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length

# Brute
# T.C. - O(N)+O(max(nums)+k)
# S.C  - O(N)

# Intuition
# convert the given array to a set
# declare 2 var count and i
# start a loop until count becomes
# k,keep checking if i is present in
# set or not otherwise increment count
# if i not present,atlast return i-1


from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        i = 1
        seen_elem = set(arr)

        while count < k:
            if i not in seen_elem:
                count += 1
            i += 1

        return i - 1


# Better
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# One thing to note,is that since array is sorted and we
# are asked to find kth missing element, what we will do is
# find the count of the missing elemnt at every index,if at
# any index we see more missing element than given k we stop
# Formula for ith index missing count is nothing we just
# ask ourself how many number are there just previous of me
# if 6 ->then 5 numbers are before 6 (1,2,3,4,5) and then ask
# how an numbers are present in original array , then we can
# make a formula of missing count: (arr[i]-1-i),atlast we calculate
# how many missing are left to explore with k-curr_missing_count
# then we add the number(prev number just before the count exceeded k)+k-curr_missing_count

from typing import List


class Solution:
    def get_missing_count(self, idx: int, arr: list[int]) -> int:
        return arr[idx] - 1 - idx

    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev_idx = -1

        for i in range(len(arr)):
            if self.get_missing_count(i, arr) >= k:
                break
            else:
                prev_idx = i

        left_missing = k - self.get_missing_count(prev_idx, arr)
        return arr[prev_idx] + left_missing


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# One thing to note,is that since array is sorted and we
# are asked to find kth missing element, what we will do is
# find the count of the missing elemnt at every index,if at
# any index we see more missing element than given k we stop
# Formula for ith index missing count is nothing we just
# ask ourself how many number are there just previous of me
# if 6 ->then 5 numbers are before 6 (1,2,3,4,5) and then ask
# how an numbers are present in original array , then we can
# make a formula of missing count: (arr[i]-1-i),atlast we calculate
# how many missing are left to explore with k-curr_missing_count
# then we add the number(prev number just before the count exceeded k)+k-curr_missing_count
# Do a binary search if at any index we see we are getting missing count
# more then we move left otherwise we move right, we are doing a lower bound
# linear search and biasing to the left direction,since we are biasing to left
# direction and moving the right pointer to the left , then we will calculate
# our final answer based on the right index value


from typing import List


class Solution:
    def get_missing_count(self, idx: int, arr: list[int]) -> int:
        return arr[idx] - 1 - idx

    def findKthPositive(self, arr: List[int], k: int) -> int:
        st, en = 0, len(arr) - 1

        while st <= en:
            mid = st + (en - st) // 2

            miss_count = self.get_missing_count(mid, arr)

            if miss_count < k:
                st = mid + 1
            else:
                en = mid - 1

        left_missing = k - self.get_missing_count(en, arr)
        return arr[en] + left_missing
