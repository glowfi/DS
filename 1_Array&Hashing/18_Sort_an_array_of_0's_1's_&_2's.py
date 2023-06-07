# https://leetcode.com/problems/sort-colors/,Medium

# Brute
# T.C. -> O(nlog(n))
# S.C. -> O(n)


class Solution:
    def mergeSort(self, l, h, arr):
        if l >= h:
            return
        mid = (l + h) // 2
        self.mergeSort(l, mid, arr)
        self.mergeSort(mid + 1, h, arr)
        self.merge(l, mid, h, arr)

    def merge(self, l, m, h, arr):
        i, j = l, m + 1
        s1, s2 = m, h
        tmp = []

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
        for i in range(l, h + 1):
            arr[i] = tmp[k]
            k += 1

    def sortColors(self, nums: List[int]) -> None:
        self.mergeSort(0, len(nums) - 1, nums)


# Better
# T.C. -> O(n)+O(n)
# S.C. -> O(3)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0, c1, c2 = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] == 1:
                c1 += 1
            elif nums[i] == 2:
                c2 += 1

        idx = 0
        for i in range(c0):
            nums[idx] = 0
            idx += 1
        for i in range(c1):
            nums[idx] = 1
            idx += 1
        for i in range(c2):
            nums[idx] = 2
            idx += 1


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        mid = 0
        high = len(nums) - 1
        low = 0

        for i in range(len(nums)):
            # if unsorted portion has zero
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # if unsorted portion has one
            elif nums[mid] == 1:
                mid += 1

            # if unsorted portion has two
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
