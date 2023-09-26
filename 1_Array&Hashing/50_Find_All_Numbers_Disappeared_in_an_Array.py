# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/ , Easy

# Brute
# T.C. - O(n^2)
# S.C  - O(1)


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hmap = {}
        ans = []

        for i in range(1, len(nums) + 1):
            found = 0
            for j in range(len(nums)):
                if nums[j] == i:
                    found = 1
                    break
            if found == 0:
                ans.append(i)

        return ans


# Better
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hmap = {}

        for i in range(1, len(nums) + 1):
            hmap[i] = 0

        for i in range(len(nums)):
            hmap[nums[i]] = 1

        ans = []
        for i in hmap:
            if hmap[i] == 0:
                ans.append(i)

        return ans


# Optimal
# T.C. - O(2n)
# S.C  - O(1)


class Solution:
    def sort(self, arr):
        idx = 0

        while idx < len(arr):
            actualPos = arr[idx] - 1

            # If the number at current index is not in its actual Position
            if arr[actualPos] != arr[idx]:
                arr[actualPos], arr[idx] = arr[idx], arr[actualPos]
            else:
                idx += 1

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        self.sort(nums)
        ans = []

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(i + 1)

        return ans
