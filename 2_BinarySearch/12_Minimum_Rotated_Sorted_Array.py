# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/,Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def findMin(self, nums):
        mn = float("inf")

        for i in range(len(nums)):
            if nums[i] < mn:
                mn = nums[i]

        return mn


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def findMin(self, nums):
        st, en = 0, len(nums) - 1
        N = len(nums)

        while st <= en:
            mid = (st + en) // 2

            prev = (mid + N - 1) % N
            nxt = (mid + 1) % N

            # Minimum element is smaller than both of its neighbour
            if nums[mid] <= nums[prev] and nums[mid] <= nums[nxt]:
                return nums[mid]

            # Identify Unsorted part as minimum element will always lie there (By observation)

            # Right is Unsorted
            elif nums[mid] >= nums[en]:
                st = mid + 1

            else:
                en = mid - 1
