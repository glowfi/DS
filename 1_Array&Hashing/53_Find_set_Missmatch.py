# https://leetcode.com/problems/set-mismatch/ , Easy

# Brute
# T.C. - O(n^2)
# S.C  - O(1)


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hmap = {}
        ans = [-1, -1]

        for i in range(1, len(nums) + 1):
            c = 0
            found = 0
            for j in range(len(nums)):
                if i == nums[j]:
                    found = 1
                    c += 1

            if c == 2:
                ans[0] = i
            elif found == 0:
                ans[1] = i

        return ans


# Better
# T.C. - O(3n)
# S.C  - O(n)


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hmap = {}
        ans = [-1, -1]

        for i in range(1, len(nums) + 1):
            hmap[i] = 0

        for j in range(len(nums)):
            hmap[nums[j]] += 1

        for k in hmap:
            if hmap[k] == 0:
                ans[1] = k
            elif hmap[k] >= 2:
                ans[0] = k

        return ans


# Optimal
# T.C. - O(2n)
# S.C  - O(1)


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        idx = 0

        while idx < len(nums):
            actualPos = nums[idx] - 1
            if nums[actualPos] != nums[idx]:
                nums[actualPos], nums[idx] = nums[idx], nums[actualPos]
            else:
                idx += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return [nums[i], i + 1]
