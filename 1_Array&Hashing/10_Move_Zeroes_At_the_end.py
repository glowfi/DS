# https://leetcode.com/problems/move-zeroes/,Easy

# Brute
# T.C. -> O(n)+O(nofzeroes)+O(n)
# S.C. -> O(n)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        tmp = []
        c = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                tmp.append(nums[i])

        for i in range(c):
            tmp.append(0)

        nums[:] = tmp[:]


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
