# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/ , Medium

# Brute
# T.C. -> O(max(nums)*n)
# S.C. -> O(1)


class Solution:
    def iswithinThreshold(self, arr, threshold, divisor):
        sm = 0
        for i in range(len(arr)):
            sm += arr[i] // divisor
            if arr[i] % divisor != 0:
                sm += 1
        return sm <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for divisor in range(1, max(nums) + 1):
            if self.iswithinThreshold(nums, threshold, divisor):
                return divisor
        return -1


# Optimal
# T.C. -> O(log(max(n))*n)
# S.C. -> O(1)


class Solution:
    def iswithinThreshold(self, arr, threshold, divisor):
        sm = 0
        for i in range(len(arr)):
            sm += arr[i] // divisor
            if arr[i] % divisor != 0:
                sm += 1
        return sm <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        st, en = 1, max(nums)

        while st <= en:
            mid = st + (en - st) // 2

            if self.iswithinThreshold(nums, threshold, mid):
                en = mid - 1
            else:
                st = mid + 1
        return st
