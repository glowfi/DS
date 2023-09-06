# https://leetcode.com/problems/search-insert-position/,Easy

# Find Lower Bound

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        st, en = 0, len(nums) - 1
        ans = len(nums)

        while st <= en:
            mid = st + (en - st) // 2
            if nums[mid] >= target:
                ans = mid
                en = mid - 1
            else:
                st = mid + 1

        return ans
