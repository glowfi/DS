# https://leetcode.com/problems/find-all-duplicates-in-an-array/ , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(1)


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(nums) + 1):
            count = 0
            for j in range(len(nums)):
                if i == nums[j]:
                    count += 1
                if count >= 2:
                    ans.append(i)
                    break

        return ans


# Better
# T.C. - O(2n)
# S.C  - O(n)


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        hmap = {}

        for i in range(1, len(nums) + 1):
            hmap[i] = 0

        for j in range(len(nums)):
            hmap[nums[j]] += 1
            if hmap[nums[j]] >= 2:
                ans.append(nums[j])

        return ans


# Optimal
# T.C. - O(2n)
# S.C  - O(1)


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        idx = 0
        ans = []

        while idx < len(nums):
            actualPos = nums[idx] - 1
            if nums[actualPos] != nums[idx]:
                nums[actualPos], nums[idx] = nums[idx], nums[actualPos]
            else:
                idx += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(nums[i])

        return ans
