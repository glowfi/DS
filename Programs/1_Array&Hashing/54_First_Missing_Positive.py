# https://leetcode.com/problems/first-missing-positive/  , Hard

# Brute
# T.C. - O(max(n)^2)
# S.C  - O(1)


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1, max(nums) + 2):
            found = 0
            for j in range(len(nums)):
                if nums[j] <= 0:
                    continue
                elif i == nums[j]:
                    found = 1
                    break
            if found == 0:
                return i

        return 1


# Better
# T.C. - O(max(n))
# S.C  - O(max(n))


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hmap = {}

        for i in range(1, max(nums) + 2):
            hmap[i] = 0

        for j in range(len(nums)):
            if nums[j] <= 0:
                continue
            hmap[nums[j]] += 1

        for k in hmap:
            if hmap[k] == 0:
                return k

        return 1


# Optimal
# T.C. - O(2n)
# S.C  - O(1)


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx = 0

        while idx < len(nums):
            actualPos = nums[idx] - 1

            if nums[idx] < len(nums) and nums[idx] > 0 and nums[actualPos] != nums[idx]:
                nums[actualPos], nums[idx] = nums[idx], nums[actualPos]
            else:
                idx += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        mx = max(nums)
        return mx + 1
