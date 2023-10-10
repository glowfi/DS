# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/,Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def findMin(self, nums):
        mn = float("inf")
        for i in range(len(nums)):
            mn = min(mn, nums[i])
        return mn


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        st, en = 1, n - 2

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]

            # Identify the unsorted part as the min element will always lie in the unsorted half for a given mid idex

            # Right half is sorted
            elif nums[mid] < nums[en]:
                en = mid - 1

            # Left half is sorted
            else:
                st = mid + 1

        if nums[0] < nums[n - 1]:
            return nums[0]
        return nums[n - 1]
