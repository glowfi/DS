# https://leetcode.com/problems/find-peak-element/description/ , Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i + 1]:
                    return i

            if i == len(nums) - 1:
                if nums[i] > nums[i - 1]:
                    return i

            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0

        st, en = 0, len(nums) - 1

        while st <= en:
            mid = (st + en) // 2

            if mid > 0 and mid < len(nums) - 1:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid

                # If Left Half is Promising
                elif nums[mid - 1] > nums[mid] and nums[mid - 1] > nums[mid + 1]:
                    en = mid - 1

                # If Right Half is Promising
                else:
                    st = mid + 1

            elif mid == 0:
                if nums[0] > nums[1]:
                    return 0
                return 1

            elif mid == len(nums) - 1:
                if nums[len(nums) - 1] > nums[len(nums) - 2]:
                    return len(nums) - 1
                return len(nums) - 2
