# https://leetcode.com/problems/rearrange-array-elements-by-sign , Medium

# Question
# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


# Example 1:

# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Explanation:
# The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
# The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
# Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.
# Example 2:

# Input: nums = [-1,1]
# Output: [1,-1]
# Explanation:
# 1 is the only positive integer and -1 the only negative integer in nums.
# So nums is rearranged to [1,-1].


# Constraints:

# 2 <= nums.length <= 2 * 10^5
# nums.length is even
# 1 <= |nums[i]| <= 10^5
# nums consists of equal number of positive and negative integers.


# Brute
# T.C. - O(N)+O(N) ~ O(N)
# S.C  - O(N/2)+O(N/2)+O(N) ~ O(2N)

# Intuition
# Store all the positive,negative numbers in 2 seperate list
# since array consists of equal number of positive and negative integers
# so we are sure that at even index we will have positive number and
# at odd index we will have negative numbers


from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []

        for num in nums:
            if num < 0:
                neg.append(num)
            if num >= 0:
                pos.append(num)

        ans = []
        posIdx, negIdx = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(pos[posIdx])
                posIdx += 1
            else:
                ans.append(neg[negIdx])
                negIdx += 1

        return ans


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# since array consists of equal number of positive and negative integers
# so we are sure that at even index we will have positive number and
# at odd index we will have negative numbers
# keep track of next positive index and next negative index

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]

        posIdx = 0
        negIdx = 1

        for i in range(len(nums)):
            if nums[i] >= 0:
                ans[posIdx] = nums[i]
                posIdx += 2
            else:
                ans[negIdx] = nums[i]
                negIdx += 2

        return ans
