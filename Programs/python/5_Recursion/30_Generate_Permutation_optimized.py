# https://leetcode.com/problems/permutations/ , Medium

# Recursive Tree
# https://0x0.st/HwTD.680.png


# Brute [Ans in argument]
# T.C. - O(n!)
# S.C  - O(n)


class Solution:
    def generate(self, idx: int, nums: list[int], ans: list[list[int]]):
        if idx == len(nums):
            ans.append(nums[:])
            return

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.generate(idx + 1, nums, ans)
            nums[i], nums[idx] = nums[idx], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.generate(0, nums, ans)
        return ans


# Brute [Ans in body]
# T.C. - O(n!)
# S.C  - O(n)


class Solution:
    def generate(self, idx: int, nums: list[int]) -> list[list[int]]:
        if idx == len(nums):
            return [nums[:]]

        ans = []

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            vals = self.generate(idx + 1, nums)
            for val in vals:
                ans.append(val[:])
            nums[i], nums[idx] = nums[idx], nums[i]

        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.generate(0, nums)
