# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/,Easy

# Brute
# T.C. -> O(nlog(n))+O(n*n)
# S.C. -> O(1)


class Solution:
    def check(self, nums: List[int]) -> bool:
        tmp = nums[:]
        tmp.sort()

        idx = 1
        while idx <= len(tmp):
            for i in range(len(nums) - 1):
                tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
            if tmp == nums:
                return True
            idx += 1

        return False


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def check(self, nums: List[int]) -> bool:
        peak = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                peak += 1
            if peak > 1:
                return False

        if nums[-1] <= nums[0] and peak <= 1:
            return True

        # Handle [1,2,3,4]
        return peak == 0
