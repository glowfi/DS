# https://leetcode.com/problems/next-greater-element-ii/ , Medium


# Optimal
# T.C. - O(2n)
# S.C  - O(n)


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        ngc = [-1] * len(nums)

        for i in range(2 * len(nums) - 1, -1, -1):
            idx = (i) % len(nums)
            while stk and nums[stk[-1]] <= nums[idx]:
                stk.pop(-1)

            if i < len(nums):
                if stk:
                    ngc[idx] = nums[stk[-1]]

            stk.append(idx)

        return ngc
