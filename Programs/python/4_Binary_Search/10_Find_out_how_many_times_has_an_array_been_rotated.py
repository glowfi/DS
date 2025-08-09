# https://www.geeksforgeeks.org/problems/rotation4723/1 , Easy, BS-In-Rotated-Sorted-Array

# Question
# Given an increasing sorted rotated array arr of distinct integers. The array is right-rotated k times. Find the value of k.
# Let's suppose we have an array arr = [2, 4, 6, 9], so if we rotate it by 2 times so that it will look like this:
# After 1st Rotation : [9, 2, 4, 6]
# After 2nd Rotation : [6, 9, 2, 4]

# Examples:

# Input: arr = [5, 1, 2, 3, 4]
# Output: 1
# Explanation: The given array is 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.

# Input: arr = [1, 2, 3, 4, 5]
# Output: 0
# Explanation: The given array is not rotated.

# Constraints:
# 1 ≤ arr.size() ≤10^5
# 1 ≤ arri ≤ 10^7

# Brute
# T.C. - O(N^2)+O(Nlog(N))
# S.C  - O(N)

# Intuition
# Keep left rotating the arr by 1
# maintain count of rotatios
# if target array is reached then return


from typing import List


class Solution:
    def left_rotate(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr

    def findKRotation(self, arr: List[int]):
        c = 0
        target_arr = sorted(arr)
        if arr == target_arr:
            return c

        for i in range(len(arr)):
            arr = self.left_rotate(arr)
            c += 1
            if arr == target_arr:
                return c

        return c


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Find min element index


from typing import List


class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        st, en = 0, len(nums) - 1
        ans = float("inf")
        index = -1

        while st <= en:
            mid = st + (en - st) // 2

            # if we cross the rotated point
            if nums[st] <= nums[mid] and nums[mid] <= nums[en]:
                if nums[st] < ans:
                    index = st
                    ans = nums[st]
                break

            # if left is sorted
            if nums[st] <= nums[mid]:
                # discard sorted half and move to unsorted
                if nums[st] < ans:
                    index = st
                    ans = nums[st]
                st = mid + 1

            # right is sorted
            else:
                # discard sorted half and move to unsorted
                if nums[mid] < ans:
                    index = mid
                    ans = nums[mid]
                en = mid - 1

        return index

    def findKRotation(self, arr: list[int]):
        return self.findMinIndex(arr)
