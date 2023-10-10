# https://leetcode.com/problems/reverse-pairs/description/ , Hard

# i<j and arr[i]>2*arr[j]

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j] * 2:
                    c += 1
        return c


# Optimal
# T.C. -> O(nlog(n))+O(n+m)
# S.C. -> O(n)


class Solution:
    def merge(self, arr, l, m, r, co):
        i, j = l, m + 1
        s1 = m
        s2 = r
        tmp = []

        idx = m + 1
        prevCount = 0
        for ii in range(l, m + 1):
            c = 0
            for jj in range(idx, r + 1):
                if arr[ii] > arr[jj] * 2:
                    c += 1
                else:
                    break
                idx += 1
            prevCount += c
            co[0] += prevCount

        while i <= s1 and j <= s2:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            elif arr[j] <= arr[i]:
                tmp.append(arr[j])
                j += 1

        while i <= s1:
            tmp.append(arr[i])
            i += 1

        while j <= s2:
            tmp.append(arr[j])
            j += 1

        k = 0
        for i in range(l, r + 1):
            arr[i] = tmp[k]
            k += 1

    def mergeSort(self, arr, l, r, c):
        if l >= r:
            return

        mid = (l + r) // 2

        self.mergeSort(arr, l, mid, c)
        self.mergeSort(arr, mid + 1, r, c)
        self.merge(arr, l, mid, r, c)

    def reversePairs(self, nums: List[int]) -> int:
        c = [0]
        self.mergeSort(nums, 0, len(nums) - 1, c)
        return c[0]
