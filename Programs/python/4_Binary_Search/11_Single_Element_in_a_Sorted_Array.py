# https://leetcode.com/problems/single-element-in-a-sorted-array, Medium, Observation

# Question
# You are given a sorted numsay consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.


# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10


# Constraints:

# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5

# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# xor out every element and
# then return


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        return xor


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# o e o e o e o e o e o
# 0,0,1,1,2,3,3,4,4,8,8
#
# o-> odd idx
# e-> even idx
#
# if i am at right of single element then if i am at even index
# and the next adjacent number is also same then i am at right side
# of the single element then i will move to left.
# if iam at left of single element then if i am at odd index and
# the next adjacent number is also same the i am at left side of
# the single element then i will move to the right.


from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        st, en = 1, len(nums) - 2

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # if odd index
            if mid % 2 == 1:
                # If at right half
                if (mid + 1) % 2 == 0 and nums[mid] == nums[mid + 1]:
                    en = mid - 1
                # If at left half
                else:
                    st = mid + 1

            # if even index
            else:
                # If at left half
                if (mid + 1) % 2 == 1 and nums[mid] == nums[mid + 1]:
                    st = mid + 1
                # If at right half
                else:
                    en = mid - 1

        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]
