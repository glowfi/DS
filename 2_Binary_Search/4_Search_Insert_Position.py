# https://leetcode.com/problems/search-insert-position/,Easy


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def searchInsert(self, nums, target):
        ans = len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                ans = i
                break
        return ans


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def searchInsert(self, nums, target):
        ans = len(nums)
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = (st + en) // 2

            if nums[mid] < target:
                st = mid + 1

            elif nums[mid] >= target:
                ans = mid
                en = mid - 1

        return ans
