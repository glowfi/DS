# https://leetcode.com/problems/find-the-duplicate-number/ , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(1, len(nums) + 1):
            c = 0
            for j in range(len(nums)):
                if nums[j] == i:
                    c += 1
                if c >= 2:
                    return i


# Better
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hmap = {}
        for i in range(1, len(nums) + 1):
            hmap[i] = 0

        for j in range(len(nums)):
            hmap[nums[j]] += 1
            if hmap[nums[j]] >= 2:
                return nums[j]


# Optimal
# T.C. - O(2n)
# S.C  - O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = 0

        while idx < len(nums):
            actualPos = nums[idx] - 1
            if nums[actualPos] != nums[idx]:
                nums[actualPos], nums[idx] = nums[idx], nums[actualPos]
            else:
                idx += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return nums[i]


# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = 0

        while idx < len(nums):
            actualPos = nums[idx] - 1
            if nums[actualPos] != nums[idx]:
                nums[actualPos], nums[idx] = nums[idx], nums[actualPos]
            else:
                idx += 1

        return nums[-1]
