# https://www.codingninjas.com/studio/problems/reverse-an-array_8365444 , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(n)

from typing import *


def helper(idx, nums):
    if idx == len(nums) // 2:
        return

    n = len(nums)
    nums[idx], nums[n - idx - 1] = nums[n - idx - 1], nums[idx]
    helper(idx + 1, nums)


def reverseArray(n: int, nums: List[int]) -> List[int]:
    helper(0, nums)
    return nums


ls = [1, 2, 3, 4]
reverseArray(len(ls), ls)
print(ls)
