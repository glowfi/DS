# https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1, Medium, MergeSort

# Question
# Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order
# without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

# Examples:

# Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
# Output:
# 2 2 3 4
# 7 10
# Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10

# Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
# Output:
# 1 2 3 5 8 9
# 10 13 15 20
# Explanation: After merging two sorted arrays we get 1 2 3 5 8 9 10 13 15 20.

# Input: a[] = [0, 1], b[] = [2, 3]
# Output:
# 0 1
# 2 3
# Explanation: After merging two sorted arrays we get 0 1 2 3.

# Constraints:
# 1 <= a.size(), b.size() <= 10^5
# 0 <= a[i], b[i] <= 10^7


# Optimal
# T.C. - O((M+N) + M*log(M) + N*log(N))
# S.C  - O(1)

# Intuition
# use 2 pointers
# fix one pointer to the last index of 1st array
# fix another pointer to the first index if 2nd array
# keep comparing if the j is smaller than i swap
# otherwise break


class Solution:
    def mergeArrays(self, a: list[int], b: list[int]) -> None:
        i = len(a) - 1
        j = 0

        while i >= 0 and j < len(b) and b[j] < a[i]:
            b[j], a[i] = a[i], b[j]
            j += 1
            i -= 1

        a.sort()
        b.sort()
