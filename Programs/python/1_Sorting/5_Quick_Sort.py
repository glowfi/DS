# https://www.geeksforgeeks.org/problems/quick-sort/1, Medium, Basic

# Question
# Implement Quick Sort, a Divide and Conquer algorithm, to sort an array, arr[] in ascending order. Given an array, arr[], with starting index low and ending index high, complete the functions partition() and quickSort(). Use the last element as the pivot so that all elements less than or equal to the pivot come before it, and elements greater than the pivot follow it.

# Note: The low and high are inclusive.

# Examples:

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: After sorting, all elements are arranged in ascending order.

# Input: arr[] = [2, 1, 6, 10, 4, 1, 3, 9, 7]
# Output: [1, 1, 2, 3, 4, 6, 7, 9, 10]
# Explanation: Duplicate elements (1) are retained in sorted order.

# Input: arr[] = [5, 5, 5, 5]
# Output: [5, 5, 5, 5]
# Explanation: All elements are identical, so the array remains unchanged.

# Constraints:
# 1 <= arr.size() <= 10^5
# 1 <= arr[i] <= 10^5


# Optimal
# T.C. - O(Nlog(N))
# S.C  - O(1)

# Intuition
# This algorithms avg,best time complexity is O(Nlog(N)) and worst case
# time complexity is O(N^2).
# This is a unstable sorting algo.
# We pick a pivot,pivot can be first,last element.we try to place all
# the elements smaller to pivot to its left and bigger to right,
# now this two partions (left and right) created are sorted recursively with the same logic.
# take 2 pointers i and j i points to start and j points to end given in the function call.
# for finding pivot find the first smallest from right anf first biggest from left.
# keep doing this till i<j and swap after every finding of these two position.
# atlast place pivot at its correct place swap pivot with j and return j.


class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr: list[int], low: int, high: int):
        if low >= high:  # return if has only one element
            return

        pivot = self.partitionv2(arr, low, high)
        self.quickSort(arr, low, pivot - 1)
        self.quickSort(arr, pivot + 1, high)

    def partitionv2(self, arr: list[int], low: int, high: int) -> int:  # algorithmic
        i, j = low, high
        pivot = arr[low]

        while i < j:
            # bigger from left
            while i < high and arr[i] <= pivot:
                i += 1

            # smaller from right
            while j > low and arr[j] > pivot:
                j -= 1

            # swap only of i<j
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # place the pivot in its correct place
        arr[low], arr[j] = arr[j], arr[low]

        return j

    # Naive way of partitioning [last as pivot]
    def partitionv1_0(self, arr: list[int], low: int, high: int) -> int:
        piv = arr[high]
        left_arr = []
        right_arr = []

        for i in range(low, high):  # ignore the last element
            if arr[i] <= piv:
                left_arr.append(arr[i])
            else:
                right_arr.append(arr[i])

        tmp_arr = [*left_arr, piv, *right_arr]

        idx = 0
        for i in range(low, high + 1):
            arr[i] = tmp_arr[idx]
            idx += 1

        return low + len(left_arr)

    # Naive way of partitioning [first as pivot]
    def partitionv1_1(self, arr: list[int], low: int, high: int) -> int:
        piv = arr[low]
        left_arr = []
        right_arr = []

        for i in range(low + 1, high + 1):  # ignore the first element
            if arr[i] <= piv:
                left_arr.append(arr[i])
            else:
                right_arr.append(arr[i])

        tmp_arr = [*left_arr, piv, *right_arr]

        idx = 0
        for i in range(low, high + 1):
            arr[i] = tmp_arr[idx]
            idx += 1

        return low + len(left_arr)
