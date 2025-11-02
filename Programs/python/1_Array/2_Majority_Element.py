# https://leetcode.com/problems/majority-element, Easy, Boyer–Moore Majority Vote Algorithm

# Question
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Brute
# T.C. - O(n^2)
# S.C  - O(1)

# Intuition
# For each element try to find out the number of times it occur
# If its count is greater than n/2 , then its the majority element

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_element = -1
        n = len(nums)

        for i in range(len(nums)):
            c = 1
            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[i] == nums[j]:
                    c += 1

            if c > n // 2:
                major_element = nums[i]

        return major_element


# Better
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# Store the frequency of each number in a hashmap
# Identify the number with frequency more than n//2
# Number with frequency n//2 is the majority element

from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        major_element = -1
        n = len(nums)
        for num, val in freq_map.items():
            if val > n // 2:
                return num

        return major_element


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
# aksed to find element occuring more than floor(n/2), what we can
# do is that think like this if "1" gets 4 votes and "2" gets 2 votes
# then 2 votes of "1" gets cancelled by 2 votes of "2".So "1" is in
# majority by 2.
# We start by assuming the first element is the major element
# we maintain the count of current majority element
# if we encounter a different element we reduce the count
# if the count becomes zero then the current element becomes majority with count reset
# to 1

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        major_element = None

        for i in range(len(nums)):
            if c == 0:
                c = 1
                major_element = nums[i]
            elif nums[i] == major_element:
                c += 1
            elif nums[i] != major_element:
                c -= 1

        return major_element
