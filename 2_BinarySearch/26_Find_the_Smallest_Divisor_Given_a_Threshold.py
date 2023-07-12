# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/ , Medium

# Brute
# T.C. -> O(max(nums)*n)
# S.C. -> O(1)


class Solution:
    def getVal(self, arr, currDivisor):
        s = 0
        for i in range(len(arr)):
            s += arr[i] // currDivisor
            if arr[i] % currDivisor != 0:
                s += 1
        return s

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        for i in range(1, max(nums) + 1):
            if self.getVal(nums, i) <= threshold:
                return i
        return -1


# Optimal
# T.C. -> O(log(max(n))*n)
# S.C. -> O(1)


class Solution:
    def getVal(self, arr, currDivisor):
        s = 0
        for i in range(len(arr)):
            s += arr[i] // currDivisor
            if arr[i] % currDivisor != 0:
                s += 1
        return s

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        st, en = 1, max(nums)
        while st <= en:
            mid = st + ((en - st) // 2)
            if self.getVal(nums, mid) <= threshold:
                en = mid - 1
            else:
                st = mid + 1
        return st
