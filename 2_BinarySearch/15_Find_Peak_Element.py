# https://leetcode.com/problems/find-peak-element/description/ , Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        st, en = 1, n - 2

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            # Find the most promising candidate which has the potential of being peak

            # if Right Neighbour is promising
            elif nums[mid + 1] > nums[mid] and nums[mid + 1] > nums[mid - 1]:
                st = mid + 1

            # if Left Neighbour is promising
            else:
                en = mid - 1

        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[n - 1] > nums[n - 2]:
            return n - 1
