# https://leetcode.com/problems/split-array-largest-sum/ , Hard

# Brute
# T.C. -> O((sum(arr)-max(arr))*n)
# S.C. -> O(1)


class Solution:
    def getParts(self, arr, k, maxSum):
        sm = 0
        parts = 1

        for i in range(len(arr)):
            if arr[i] + sm <= maxSum:
                sm += arr[i]
            else:
                parts += 1
                sm = arr[i]

        return parts

    def splitArray(self, nums: List[int], k: int) -> int:
        st, en = max(nums), sum(nums) + 1

        for minSum in range(st, en):
            if self.getParts(nums, k, minSum) == k:
                return minSum
        return st


# Optimal
# T.C. -> O(log(sum(arr)-max(arr))*n)
# S.C. -> O(1)


class Solution:
    def getParts(self, nums, k, maxSum):
        sm = 0
        parts = 1

        for i in range(len(nums)):
            if nums[i] + sm <= maxSum:
                sm += nums[i]
            else:
                parts += 1
                sm = nums[i]

        return parts

    def splitArray(self, nums: List[int], k: int) -> int:
        st, en = max(nums), sum(nums)

        while st <= en:
            mid = st + (en - st) // 2

            if self.getParts(nums, k, mid) > k:
                st = mid + 1
            else:
                en = mid - 1

        return st
