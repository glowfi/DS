# https://leetcode.com/problems/container-with-most-water, Medium, TwoPointers / Greedy

# Question
# You are given an integer array height of length n. There are n vertical lines drawn such that the
# two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1


# Constraints:
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

# Brute
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# Find all the possble container's water storing
# capacity and take the max among them

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx_area = float("-inf")
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                w = (j - i) + 1
                h = min(height[i], height[j])
                area = w * h
                mx_area = max(mx_area, area)

        return mx_area


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# Our goal is to maximize the area but maximizing width and height
# We want two lines that form the container with the maximum area.
# The area is determined by:
#   area = (right_index - left_index) * min(height[left], height[right])
#
# We place two pointers at the extremes: left (l) at 0 and right (r) at n-1,
# to maximize width
# At each step, we compute the current area and update the maximum.
#
# The key decision is: which pointer to move?
# - The height of the container is limited by the shorter line.
# - If we move the taller line inward, the width shrinks, but the height
#   cannot increase beyond the shorter line we kept, so area cannot improve
#   because height is still bounded by the same or a smaller value.
# - If instead we move the shorter line inward, there is a chance of
#   finding a taller line that can compensate for the reduced width and
#   give a larger area.

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mx_area = float("-inf")

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            mx_area = max(mx_area, w * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return mx_area
