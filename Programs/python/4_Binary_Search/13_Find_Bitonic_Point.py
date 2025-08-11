# https://www.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1, Easy, Observation

# Question
# Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
# Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.

# Note: It is guaranteed that the array contains exactly one bitonic point.

# Examples:

# Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
# Output: 8
# Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 50
# Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.

# Input: arr[] = [120, 100, 80, 20, 0]
# Output: 120
# Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].

# Constraints:
# 3 ≤ arr.size() ≤ 10^5
# 1 ≤ arr[i] ≤ 10^6

# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# just check which element is greater
# than 2 of its neighbour in single
# pass


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            if i == 0 and nums[0] > nums[1]:
                return nums[0]
            elif i == len(nums) - 1 and nums[len(nums) - 1] > nums[len(nums) - 2]:
                return nums[len(nums) - 1]

            elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return nums[i]

    def findMaximum(self, arr: list[int]):
        return self.findPeakElement(arr)


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Find peak element using BS


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        st, en = 1, len(nums) - 2

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return nums[mid]

            # Find promising canditate in which direction we can find peak

            # if Right Neighbour is promising
            if nums[mid + 1] > nums[mid] and nums[mid + 1] > nums[mid]:
                st = mid + 1

            else:
                # if Left Neighbour is promising
                en = mid - 1

        if len(nums) == 1:
            return nums[0]

        if nums[0] > nums[1]:
            return nums[0]

        if nums[-1] > nums[-2]:
            return nums[len(nums) - 1]

    def findMaximum(self, arr: list[int]):
        return self.findPeakElement(arr)
