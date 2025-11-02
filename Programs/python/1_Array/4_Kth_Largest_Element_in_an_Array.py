# https://leetcode.com/problems/kth-largest-element-in-an-array, Medium, Heap / QuickSelect

# Question
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


# Constraints:
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

# Brute
# T.C. - O(nlog(n))
# S.C  - O(n)

# Intuition
# Sort the array in descending and return the kth element from first

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


# Better
# T.C. - O(nlog(k))
# S.C  - O(k)

# Intuition
# Use a Min heap and keep
# maintaining a min heap of size k
# atlast at top will be your
# kth largest element

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap: list[int] = []

        for i in range(len(nums)):
            elem = nums[i]
            heapq.heappush(min_heap, elem)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# We are going to use the quick select algo
# In this algo we choose a pivot as first number
# Then we try to place all the numbers greater than
# pivot at left and all smaller at right.We try to
# mimic a descending order sort.
# The get pivot algo work as below:
# + place two pointers at given l and r range
# + only swap numbers at index l and r if they are not in correct place
# + move i, j if nums[i]>=pivot or nums[j]<=pivot
# atlast we just need to swap the jth and lth index
# You will see by swapping the jth and lth index
# autmatically all the elements greater than pivot
# gets placed to left and smaller to left
# as the jth index will become pivot now

from typing import List


class Solution:
    def get_pivot(self, l, r, nums: List[int]) -> int:
        i, j = l + 1, r
        p = nums[l]

        while i <= j:
            if nums[i] < p and nums[j] > p:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            if nums[i] >= p:
                i += 1

            if nums[j] <= p:
                j -= 1

        nums[l], nums[j] = nums[j], nums[l]
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot_index = -1

        while True:
            pivot_index = self.get_pivot(l, r, nums)
            if pivot_index == k - 1:
                break
            elif pivot_index > k - 1:
                r = pivot_index - 1
            else:
                l = pivot_index + 1

        return nums[pivot_index]
