# https://leetcode.com/problems/merge-sorted-array, Easy, Two Pointers

# Question
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[j] <= 10^9


# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# Brute
# T.C. - O(m+n)+O(m+n)
# S.C  - O(m+n)

# Intuition
# We apply the classic merge 2 sorted algorithm
# We store the data in a temporary array
# Then we copy the data from temporary array to
# nums1

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        tmp = [0] * (m + n)
        p1, p2 = 0, 0
        k = 0

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                tmp[k] = nums1[p1]
                p1 += 1
            else:
                tmp[k] = nums2[p2]
                p2 += 1
            k += 1

        while p1 < m:
            tmp[k] = nums1[p1]
            p1 += 1
            k += 1

        while p2 < n:
            tmp[k] = nums2[p2]
            p2 += 1
            k += 1

        for i in range(len(tmp)):
            nums1[i] = tmp[i]


# Optimal
# T.C. - O(m+n)
# S.C  - O(1)

# Intuition
# nums1 = [7,8,9,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Consider the above example if we still try to use the
# classic merge algo then we will see that nums2 becomes unsorted
# when 7 is swapped with 2.
# If you start merging from the front, we’ll overwrite numbers
# We are going to traverse each array from the back
# Our target is to place the largest number first in nums1
# Only if the nums1 get exhausted before nums2, then outside
# the loop we handle taking all the elements from nums2 and
# put it in the nums1 array.Dont need to do anything if nums2
# gets exhausted before nums1 as nums1 is already in sorted order

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2 = m - 1, n - 1
        k = (m + n) - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[k] = nums1[p1]
                p1 -= 1
                k -= 1
            else:
                nums1[k] = nums2[p2]
                p2 -= 1
                k -= 1

        while p2 >= 0:
            nums1[k] = nums2[p2]
            p2 -= 1
            k -= 1
