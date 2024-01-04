# https://leetcode.com/problems/house-robber-ii/ , Medium


# Space Optimized
# T.C. - O(n)
# S.C  - O(1)


class Solution:
    def solve(self, nums: List[int]) -> int:
        prev_prev = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            take, notTake = nums[i], 0

            if i - 2 >= 0:
                take += prev_prev

            if i - 1 >= 0:
                notTake = prev

            prev_prev = prev
            prev = max(take, notTake)

        return prev

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        with_first_excluded = self.solve(nums[1:])
        with_last_excluded = self.solve(nums[: len(nums) - 1])

        return max(with_first_excluded, with_last_excluded)
