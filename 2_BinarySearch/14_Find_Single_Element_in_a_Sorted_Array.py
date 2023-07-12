# https://leetcode.com/problems/single-element-in-a-sorted-array/,Medium


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
            mid = st + ((en - st) // 2)

            if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
                return nums[mid]

            # Elements in Left Half -> (even,odd)
            # Elements in Right Half -> (odd,even)

            # Identify in which half we are in

            # If index is even
            if mid % 2 == 0:
                # if we are in Left Half then next element will be equal
                if nums[mid] == nums[mid + 1]:
                    st = mid + 1
                else:
                    en = mid - 1

            # If index is odd
            else:
                # if we are in Right Half then next element will be equal
                if nums[mid] == nums[mid + 1]:
                    en = mid - 1
                else:
                    st = mid + 1
