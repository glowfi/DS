# https://leetcode.com/problems/next-permutation/,Medium

# Optimal
# T.C. -> O(n)+O(n)+O(n)=O(3n)
# S.C. -> O(1)


class Solution:
    def rev(self, i, j, nums):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        breakPoint = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                breakPoint = i
                break

        if breakPoint == -1:
            print(breakPoint)
            self.rev(0, len(nums) - 1, nums)
        else:
            for i in range(len(nums) - 1, breakPoint - 1, -1):
                if nums[i] > nums[breakPoint]:
                    nums[i], nums[breakPoint] = nums[breakPoint], nums[i]
                    break

            self.rev(breakPoint + 1, len(nums) - 1, nums)

        return nums
