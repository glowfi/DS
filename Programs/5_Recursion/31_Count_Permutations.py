# NA , Medium

# Brute [Ans in body]
# T.C. - O(n!)
# S.C  - O(n)


class Solution:
    def generate(self, idx: int, nums: list[int]) -> int:
        if idx == len(nums):
            return 1

        count = 0

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            val = self.generate(idx + 1, nums)
            count += val
            nums[i], nums[idx] = nums[idx], nums[i]

        return count

    def permute(self, nums: List[int]) -> int:
        return self.generate(0, nums)
