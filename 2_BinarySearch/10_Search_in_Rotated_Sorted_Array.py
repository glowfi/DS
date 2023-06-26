# https://leetcode.com/problems/search-in-rotated-sorted-array/,Medium

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# Better
# T.C. -> O(log(n))+O(n)
# S.C. -> O(1)


class Solution(object):
    def bs(self, arr, x, st, en):
        while st <= en:
            mid = (st + en) // 2

            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                en = mid - 1

            else:
                st = mid + 1

        return -1

    def breakPoint(self, arr):
        breakPoint = -1
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                breakPoint = i
                break
        return breakPoint

    def search(self, nums, target):
        getBreakPoint = self.breakPoint(nums)

        if getBreakPoint == -1:
            return self.bs(nums, target, 0, len(nums) - 1)

        firstHalf = self.bs(nums, target, 0, getBreakPoint - 1)
        if firstHalf != -1:
            return firstHalf
        secHalf = self.bs(nums, target, getBreakPoint, len(nums) - 1)
        return secHalf


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def search(self, nums, target):
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = (st + en) // 2

            # If target found
            if nums[mid] == target:
                return mid

            # Identify Sorted Part
            # Check if target exists in the sorted part and eliminate the part not conatining the target

            # If left half is sorted
            elif nums[st] <= nums[mid]:
                # Target is in left half
                if nums[st] <= target and target <= nums[mid]:
                    en = mid - 1
                else:
                    st = mid + 1

            # If right half is sorted
            else:
                # Target is in right half
                if nums[mid] <= target and target <= nums[en]:
                    st = mid + 1
                else:
                    en = mid - 1

        return -1
