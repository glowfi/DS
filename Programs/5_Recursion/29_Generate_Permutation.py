# https://leetcode.com/problems/permutations/ , Easy


# Brute [Ans in argument]
# T.C. - O(n!)
# S.C  - O(n)


class Solution:
    def generate(
        self,
        idx: int,
        nums: list[int],
        tmp: list[int],
        ans: list[list[int]],
        seen: dict[int, bool],
    ):
        if idx == len(nums):
            ans.append(tmp[:])
            return

        for i in range(0, len(nums)):
            if nums[i] in seen and seen[nums[i]]:
                continue
            tmp.append(nums[i])
            seen[nums[i]] = True
            self.generate(idx + 1, nums, tmp, ans, seen)
            tmp.pop(-1)
            seen[nums[i]] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.generate(0, nums, [], ans, {})
        return ans


# Brute [Ans in body]
# T.C. - O(n!)
# S.C  - O(n)


class Solution:
    def generate(
        self,
        idx: int,
        nums: list[int],
        tmp: list[int],
        seen: dict[int, bool],
    ) -> list[list[int]]:
        if idx == len(nums):
            return [tmp]

        ans = []

        for i in range(0, len(nums)):
            if nums[i] in seen and seen[nums[i]]:
                continue
            tmp.append(nums[i])
            seen[nums[i]] = True
            vals = self.generate(idx + 1, nums, tmp, seen)
            for val in vals:
                ans.append(val[:])
            tmp.pop(-1)
            seen[nums[i]] = False

        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.generate(0, nums, [], {})
