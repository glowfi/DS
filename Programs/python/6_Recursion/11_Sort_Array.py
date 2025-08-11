# https://leetcode.com/problems/sort-an-array , Medium, IBH/DivideAndConquer

# Question
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.


# Constraints:

# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4

# Brute
# T.C. - O(N^2)
# S.C  - O(N) [recursion stack space]

# Intuition
# Use IBH method
# Assume the array will get sorted from idx+1 post to end
# Just insert the element at its correct place, the current elment


from typing import List
from bisect import bisect_right


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base
        if len(nums) == 0:
            return nums

        # Hypothesis
        lastElem = nums.pop(-1)
        self.sortArray(nums)

        # Induction
        idx = bisect_right(nums, lastElem)
        nums.insert(idx, lastElem)
        return nums


# Optimal
# T.C. - O(Nlog(N))
# S.C  - O(N) [recursion stack space]

# Intuition
# Use Merge Sort [inplace]


from typing import List


class Solution:
    def merge2sortedArray(self, lo: int, mid: int, hi: int, arr: list[int]) -> None:
        i, j = lo, mid + 1

        tmp = []
        while i <= mid and j <= hi:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1

        while i <= mid:
            tmp.append(arr[i])
            i += 1

        while j <= hi:
            tmp.append(arr[j])
            j += 1

        k = 0
        for i in range(lo, hi + 1):
            arr[i] = tmp[k]
            k += 1

    def merge_sort(self, lo: int, hi: int, arr: list[int]):
        # Base
        if lo >= hi:
            return

        mid = (lo + hi) // 2

        # Hypotheis
        # Sort Left arr
        self.merge_sort(lo, mid, arr)
        # Sort Right arr
        self.merge_sort(mid + 1, hi, arr)

        # Induction
        self.merge2sortedArray(lo, mid, hi, arr)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(0, len(nums) - 1, nums)
        return nums
