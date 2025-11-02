# https://leetcode.com/problems/majority-element-ii, Medium, Boyer–Moore Majority Vote Algorithm

# Question
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1,2]
# Output: [1,2]


# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# Better
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# Store the frequency of each number in a hashmap
# Identify the number with frequency more than n//3
# Numbers with frequency n//3 is the majority element

from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        ans = []

        for num, freq in freq_map.items():
            if freq > len(nums) // 3:
                ans.append(num)

        return ans


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# We can observe something suppose we have an array of size n=6.
# For being majority element an element must occure atleast more
# than floor(n/2) i.e. say atleast 4 times.
# Example array: [1,1,1,1,2,2] . Here 4 is the majority element.
# Similary if we are supposed to fina an element occuring more
# than floor(n/3) then it must appear atleast 3 times.
# Example array: [1,1,1,2,2,2] . Here 1,2 are the majority element.
# So it is clear the max majority element we can have for n is k-1:
# n/2 -> 1
# n/3 -> 2
# n/4 -> 3
# The intuition to solve this problem is to think of a cancelling
# mechanism,if we take the array [1,1,1,1,2,2] and suppose we were
# aksed to find element occuring more than floor(n/3), what we can
# do is that think like this if "1" gets 4 votes and "2" gets 2 votes
# then 2 votes of "1" gets cancelled by 2 votes of "2".So "1" is in
# majority by 2.
# Since there can be atmose 0,1 or 2 elements
# Take this example:
# n=10
#  -------  -------
# [_ _ _  _ _ _  _ _ _  _ ]
# <n/3>  <n/3>   <n/3>
# No space to accomodate another array elements.
# We start by assuming there are 2 majority elements.
# we maintain the count of current majority elements
# if we encounter a different element we reduce the count
# if the count becomes zero then the current element becomes majority with count reset
# to 1
# After all this we do verify if it appears more than floor(n/3) times

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = 0
        major_element1 = None

        c2 = 0
        major_element2 = None

        for i in range(len(nums)):
            if nums[i] == major_element1:
                c1 += 1
            elif nums[i] == major_element2:
                c2 += 1
            elif c1 == 0:  # this must be done after
                major_element1 = nums[i]
                c1 = 1
            elif c2 == 0:  # this must be done after
                major_element2 = nums[i]
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        # Verification
        ans = []
        c1, c2 = 0, 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == major_element1:
                c1 += 1
            if nums[i] == major_element2:
                c2 += 1

        if c1 > n // 3:
            ans.append(major_element1)
        if c2 > n // 3:
            ans.append(major_element2)

        return ans
