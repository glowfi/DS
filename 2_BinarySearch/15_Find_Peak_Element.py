# https://leetcode.com/problems/find-peak-element/description/ , Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        st, en = 1, len(nums) - 2

        while st <= en:
            mid = st + ((en - st) // 2)

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            ### Find Most promising Candidate among left and right neighbour

            # Left Neighbour can be peak
            elif nums[mid - 1] > nums[mid] and nums[mid - 1] > nums[mid + 1]:
                en = mid - 1

            # Right Neighbour can be peak
            else:
                st = mid + 1
