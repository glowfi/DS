# https://leetcode.com/problems/merge-sorted-array, Easy, Two Pointers

# Question
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
# should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


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
# When merging nums2 into nums1 in-place, starting from the front can destroy data you still need.
#
# Example:
# nums1 = [2, 7, 0, 0], m = 2
# nums2 = [1, 3], n = 2
#
# If you start filling from index 0 with the smallest element, you might put 1 at nums1[0] and
# then 2 at nums1[1], but in the process you can overwrite 7 before you’ve compared it with 3.
# This makes it hard to correctly merge while preserving all elements.
#
# To avoid overwriting useful values, we go from right to left. nums1 has enough space at
# the end (the zeros) to hold all elements, so we fill from the last index:
#
# Compare the largest elements: 7 (from nums1) and 3 (from nums2); place 7 at the end.
# Then compare 2 and 3; place 3.
# Then compare 2 and 1; place 2.
# Finally place 1.
# This gives: [1, 2, 3, 7], and we never overwrite a needed element.
#
# If nums1’s initial part is exhausted before nums2 (for example, nums1 = [0,0,0], m = 0,
# nums2 = [2,5,6], n = 3), we simply copy all remaining elements from nums2 into
# nums1 from the back, which still results in a sorted array.

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2 = m - 1, n - 1
        k = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[k] = nums2[p2]
                p2 -= 1
            else:
                nums1[k] = nums1[p1]
                p1 -= 1
            k -= 1

        while p2 >= 0 and p1 < 0:
            nums1[k] = nums2[p2]
            p2 -= 1
            k -= 1
