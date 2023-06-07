# https://leetcode.com/problems/two-sum/description/,Easy

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff not in h:
                h[nums[i]] = i
            else:
                return [i, h[diff]]
