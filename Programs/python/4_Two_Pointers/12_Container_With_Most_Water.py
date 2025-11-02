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
# Now in this question we try to find the optimal
# two pairs of bars with which we get the max area.
# We are going to take two pointers l and r and place
# them at the 2 extreme ends of the array.Now we need
# to decide how we are going to move the pointers.
# One thing we can see that the min height controls
# the value of the area, so its better to move the
# bar with less area as no matter what bigger height
# we get we wont get better area.Also as we move more
# towards left the width decrease so its better to keep
# the bar with greate height intact so that in future if
# we get a greater height then it can compensate for the
# lesser width.

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mx_area = float("-inf")

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = w * h
            mx_area = max(area, mx_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return mx_area
