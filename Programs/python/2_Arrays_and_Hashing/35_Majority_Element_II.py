# https://leetcode.com/problems/majority-element-ii, Medium, Algo

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

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Keep track of the element appearing more
# than n//3 times using 2 loops


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appear_count = len(nums) // 3
        majority_elements: set[int] = set()

        for i in range(len(nums)):
            c = 1
            for j in range(len(nums)):
                if j == i:
                    continue

                if nums[i] == nums[j]:
                    c += 1

            if c > appear_count:
                majority_elements.add(nums[i])

        return list(majority_elements)


# Better
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# store the frequency of each element
# and just keep checking if some element
# occur more than n//3 times

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appear_count = len(nums) // 3
        freq_mp = {}
        majority_elements: set[int] = set()

        for num in nums:
            if num not in freq_mp:
                freq_mp[num] = 1
            else:
                freq_mp[num] += 1

            if freq_mp[num] > appear_count:
                majority_elements.add(num)

        return list(majority_elements)


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Observation - we can have atmost k-1 majority elements for n//k
# For example:
# for n=4 if n//2 given we can have only 1 majority element
# than can occur 3 times and 1 element can occur 1 time
# [1,1,1,2] for n//2
# for n=10 if n//3 given we can have only 2 majority elements
# than can occur 4 times each and 2 element can occur 1 time
# [1,1,1,1,2,2,2,2,3,3] for n//3
# 2 pass algo one to find and one to verify
# basically this algos main Intuition is element occuring more than n//2
# times will cancel out the elements occuring less number of times


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appear_count = len(nums) // 3
        maj1 = nums[0]
        c1 = 0

        maj2 = nums[0]
        c2 = 0

        for i in range(len(nums)):
            # increment count1 if its the same majority element1
            if nums[i] == maj1:
                c1 += 1

            # increment count2 if its the same majority element2
            elif nums[i] == maj2:
                c2 += 1

            elif c1 == 0:  # reset majority element1
                c1 = 1
                maj1 = nums[i]

            elif c2 == 0:  # reset majority element2
                c2 = 1
                maj2 = nums[i]

            else:
                c1 -= 1
                c2 -= 1

        c1 = 0
        c2 = 0
        for i in range(len(nums)):
            if nums[i] == maj1:
                c1 += 1
            elif nums[i] == maj2:
                c2 += 1

        ans = []

        if c1 > appear_count:
            ans.append(maj1)

        if c2 > appear_count:
            ans.append(maj2)

        return ans
