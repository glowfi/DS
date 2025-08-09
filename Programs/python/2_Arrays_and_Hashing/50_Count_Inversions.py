# https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1 , Medium, MergeSort

# Question
# Given an array of integers arr[]. Find the Inversion Count in the array.
# Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

# Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
# If an array is sorted in the reverse order then the inversion count is the maximum.

# Examples:

# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

# Input: arr[] = [2, 3, 4, 5, 6]
# Output: 0
# Explanation: As the sequence is already sorted so there is no inversion count.

# Input: arr[] = [10, 10, 10]
# Output: 0
# Explanation: As all the elements of array are same, so there is no inversion count.

# Constraints:
# 1 ≤ arr.size() ≤ 10^5
# 1 ≤ arr[i] ≤ 10^4

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Generate all subarrays and find the
# subarray with the matching condition


class Solution:
    def inversionCount(self, arr):
        c = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i < j and arr[i] > arr[j]:
                    c += 1
        return c


# Optimal
# T.C. - O(Nlog(N))
# S.C  - O(1)

# Intuition
# use merge sort to solve this
# Suppose we have 2 sorted array as below
# [5,6,7,8] [1,2,3,4]
# one thing for sure is (5,2)(5,3),(5,4)
# will form pair right as i<j and arr[i]>arr[j]
# but in merge sort after we have proceessed a smaller
# number we move one position ahead but this may lead
# to missing of many pair, so since 2 arrays are sorted
# we can for sure say if 5 forms pair then all the further
# elements will form pair too and add those pair to counter


class Solution:
    def merge(self, l: int, mid: int, h: int, arr: list[int]) -> int:
        i, j = l, mid + 1
        tmp = []

        c = 0

        while i <= mid and j <= h:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                c += mid - i + 1  # include all the farther ahead elements too
                tmp.append(arr[j])
                j += 1

        while i <= mid:
            tmp.append(arr[i])
            i += 1
        while j <= h:
            tmp.append(arr[j])
            j += 1

        k = 0
        for i in range(l, h + 1):
            arr[i] = tmp[k]
            k += 1

        return c

    def mergeSort(self, l: int, h: int, arr: list[int]) -> int:
        c = 0

        if l >= h:  # array has 1 element
            return 0

        mid = (l + h) // 2

        c += self.mergeSort(l, mid, arr)
        c += self.mergeSort(mid + 1, h, arr)
        c += self.merge(l, mid, h, arr)

        return c

    def inversionCount(self, arr: list[int]) -> int:
        return self.mergeSort(0, len(arr) - 1, arr)
