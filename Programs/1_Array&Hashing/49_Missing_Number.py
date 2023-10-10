# https://leetcode.com/problems/missing-number/ , Easy

# Brute
# T.C. - O(n^2)
# S.C  - O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums) + 1):
            found = 0
            for j in range(len(nums)):
                if i == nums[j]:
                    found = 1
                    break
            if found == 0:
                return i


# Better
# T.C. - O(3n)
# S.C  - O(n)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hmap = {}
        for i in range(0, len(nums) + 1):
            hmap[i] = 0

        for j in range(len(nums)):
            hmap[nums[j]] = 1

        for elem in hmap:
            if hmap[elem] == 0:
                return elem


# Optimal
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = n * (n + 1) // 2
        currSum = sum(nums)
        return actual - currSum


# Optimal
# T.C. - O(n)
# S.C  - O(1)


# If a number is missing then the index at which index!=element will have be the missing
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums):
            # Since zero based indexing
            actualPos = nums[idx]

            # Ignore elements greater than length of array
            if nums[idx] < len(nums) and nums[actualPos] != nums[idx]:
                nums[actualPos], nums[idx] = nums[idx], nums[actualPos]
            else:
                idx += 1

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        # Case 2 : [0,1]

        return len(nums)
