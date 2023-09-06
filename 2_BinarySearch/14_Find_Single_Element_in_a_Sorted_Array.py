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


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        st, en = 1, n - 2

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # Left Half -> (even,odd)
            # Right Half -> (odd,even)

            # 0 1 2 3 4 5 6 7 8
            # 1,1,2,3,3,4,4,8,8

            # If Odd Index
            elif mid % 2 != 0:
                # If at right half
                if (mid + 1) % 2 == 0 and nums[mid] == nums[mid + 1]:
                    en = mid - 1
                # If at left index
                else:
                    st = mid + 1

            # If Even Index
            else:
                # If at right half
                if (mid - 1) % 2 != 0 and nums[mid] == nums[mid - 1]:
                    en = mid - 1
                # If at left index
                else:
                    st = mid + 1

        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]
