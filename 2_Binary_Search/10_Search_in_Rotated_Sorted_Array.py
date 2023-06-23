# https://leetcode.com/problems/search-in-rotated-sorted-array/,Medium

# Optimal
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
