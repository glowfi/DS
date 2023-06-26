# https://leetcode.com/problems/single-element-in-a-sorted-numsay/,Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def singleNonDuplicate(self, nums):
        xor = 0

        for i in range(len(nums)):
            xor ^= nums[i]

        return xor


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]

        st, en = 1, len(nums) - 2

        while st <= en:
            mid = (st + en) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # Left Half -> (even,odd)
            # Right Half -> (odd,even)

            if (
                mid % 2 == 0
                and nums[mid + 1] == nums[mid]
                or mid % 2 == 1
                and nums[mid] == nums[mid - 1]
            ):
                st = mid + 1
            else:
                en = mid - 1
