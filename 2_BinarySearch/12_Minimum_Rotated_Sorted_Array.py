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


class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        st, en = 1, n - 2

        while st <= en:
            mid = st + ((en - st) // 2)

            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]

            # Identify the unsorted part as the minimum elemeny will be present in the unsorted part (By Observation)

            # Right Half is sorted and left half is unsorted
            elif nums[mid] < nums[en]:
                en = mid - 1

            # Left Half is sorted and right half is unsorted
            else:
                st = mid + 1

        return min(nums[0], nums[n - 1])
