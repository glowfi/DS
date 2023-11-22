# https://leetcode.com/problems/combination-sum-ii/ , Medium

# Brute
# T.C. - O(2^t*k)+O(nlog(n))
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
            if i > idx and nums[i] == nums[i - 1]:
                continue

            tmp.append(nums[i])
            if nums[i] <= target:
                self.getCombinations(i + 1, nums, tmp, target - nums[i], ans)
            tmp.pop(-1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.getCombinations(0, candidates, [], target, ans)
        return ans
