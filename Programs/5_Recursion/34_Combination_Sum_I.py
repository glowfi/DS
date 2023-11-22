# https://leetcode.com/problems/combination-sum/ , Medium

# Brute
# T.C. - O(2^t*k)
# S.C  - O(k*x)


class Solution:
    def getCombinations(
        self,
        idx: int,
        nums: list[int],
        tmp: list[int],
        target: int,
        ans: list[list[int]],
    ):
        if target == 0:
            ans.append(tmp[:])
            return

        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            if nums[i] <= target:
                self.getCombinations(i, nums, tmp, target - nums[i], ans)
            tmp.pop(-1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.getCombinations(0, candidates, [], target, ans)
        return ans
