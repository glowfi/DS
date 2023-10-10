# https://practice.geeksforgeeks.org/problems/minimum-difference-pair5444/1,Easy

# Better
# T.C. -> O(nlog(n))+O(n)
# S.C. -> O(1)


class Solution:
    def minimum_difference(self, nums):
        nums.sort()
        mn = float("inf")

        for i in range(len(nums) - 1):
            if abs(nums[i] - nums[i + 1]) < mn:
                mn = abs(nums[i] - nums[i + 1])
        return mn


# Optimal
# T.C. -> O(nlog(n))
# S.C. -> O(n)


class Solution:
    def mergeSort(self, st, en, arr, mn):
        if st >= en:
            return

        mid = (st + en) // 2

        self.mergeSort(st, mid, arr, mn)
        self.mergeSort(mid + 1, en, arr, mn)
        self.merge(st, mid, en, arr, mn)

    def merge(self, st, mid, en, arr, mn):
        i, j = st, mid + 1
        k = 0
        tmp = []

        while i <= mid and j <= en:
            if arr[i] <= arr[j]:
                mn[0] = min(mn[0], arr[j] - arr[i])
                tmp.append(arr[i])
                i += 1
            else:
                mn[0] = min(mn[0], arr[i] - arr[j])
                tmp.append(arr[j])
                j += 1

        while i <= mid:
            tmp.append(arr[i])
            i += 1

        while j <= en:
            tmp.append(arr[j])
            j += 1

        k = 0
        for i in range(st, en + 1):
            arr[i] = tmp[k]
            k += 1

    def minimum_difference(self, nums):
        min = [float("inf")]
        self.mergeSort(0, len(nums) - 1, nums, min)

        return min[0]
