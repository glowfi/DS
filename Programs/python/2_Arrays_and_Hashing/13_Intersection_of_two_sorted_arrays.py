# https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-array-1587115620/1, Easy, MergeSort

# Question
# Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.

# Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.

# Note: If there is no intersection then return an empty array.

# Examples:

# Input: arr1[] = [1, 2, 3, 4], arr2[] = [2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are only common elements in both the arrays.

# Input: arr1[] = [1, 2, 2, 3, 4], arr2[] = [2, 2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are the only common elements.

# Input: arr1[] = [1, 2], arr2[] = [3, 4]
# Output: []
# Explanation: No common elements.

# Expected Time Complexity: O(n + m)
# Expected Auxiliary Space: O(min(n,m))

#  Constraints:
# 1 <= arr1.size(),arr2.size() <= 10^5
# 1 <= arr1[i], arr2[i] <= 10^6

# Brute
# T.C. - O(m)+O(n)+O((m+n)log(m+n))+O(m+n) ~ O((m+n)log(m+n))
# S.C  - O(m+n)

# Intuition
# convert the two arrays into set
# find the intersection between them
# return the intersection converted into list in a sorted manner


class Solution:
    # Function to return a list containing the intersection of two arrays.
    def intersection(self, arr1: list[int], arr2: list[int]):
        st1 = set(arr1)
        st2 = set(arr2)

        return sorted(list(st1.intersection(st2)))


# Optimal
# T.C. - O(m+n)
# S.C  - O(1)

# Intuition
# just keep track of what you inserted last time
# dont insert if its the same element you inserted last time
# Just follow merge sort algorithm and when equal elements
# are encounter insert only based on the above condition


class Solution:

    def intersection(self, arr1: list[int], arr2: list[int]):
        intersection: list[int] = []

        i, j = 0, 0
        last_inserted = (10**9) + 1

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                if last_inserted != arr1[i]:
                    last_inserted = arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                if last_inserted != arr2[j]:
                    last_inserted = arr2[j]
                j += 1
            else:
                if last_inserted != arr1[i]:
                    last_inserted = arr1[i]
                    intersection.append(arr1[i])
                i += 1
                j += 1

        return intersection
