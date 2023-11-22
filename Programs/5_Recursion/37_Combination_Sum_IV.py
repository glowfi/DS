# https://leetcode.com/problems/combination-sum-iv/ , Medium

# Brute
# T.C. - O(2^t*k)
# S.C  - O(k*x)


class Solution:
    def getCount(self, idx, tmp, nums, target):
        if target == 0:
            return 1

        count = 0
        for i in range(0, len(nums)):
            if nums[i] <= target:
                val = self.getCount(idx, tmp, nums, target - nums[i])
                count += val

        return count

    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.getCount(0, [], nums, target)
