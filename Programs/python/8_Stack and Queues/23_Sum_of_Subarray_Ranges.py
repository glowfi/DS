# https://leetcode.com/problems/sum-of-subarray-ranges , Medium

# Brute
# T.C. - O(N^2)
# S.C  - O()


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sm = 0
        for i in range(len(nums)):
            mn, mx = nums[i], nums[i]
            for j in range(i + 1, len(nums)):
                mx = max(mx, nums[j])
                mn = min(mn, nums[j])
                sm += mx - mn

        return sm


# Optimal
# T.C. - O(10N)
# S.C  - O(10N)


class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stk = []

        for i in range(n):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop(-1)

            if stk:
                left[i] = stk[-1]

            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop(-1)

            if stk:
                right[i] = stk[-1]

            stk.append(i)

        sm = 0
        for i in range(n):
            sm = sm + ((i - left[i]) * (right[i] - i) * arr[i])

        return sm

    def sumSubarrayMaxs(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stk = []

        for i in range(n):
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop(-1)

            if stk:
                left[i] = stk[-1]

            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] < arr[i]:
                stk.pop(-1)

            if stk:
                right[i] = stk[-1]

            stk.append(i)

        sm = 0
        for i in range(n):
            sm = sm + ((i - left[i]) * (right[i] - i) * arr[i])

        return sm

    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums)
