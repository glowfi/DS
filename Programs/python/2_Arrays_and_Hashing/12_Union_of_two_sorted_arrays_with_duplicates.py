# https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1 , Medium, MergeSort

# Question
# Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

# Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.
# Examples:

# Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
# Output: 1 2 3 4 5 6 7
# Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.

# Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
# Output: 1 2 3 4 5
# Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.

# Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
# Output: 1 2
# Explanation: Distinct elements including both the arrays are: 1 2.

# Constraints:
# 1  <=  a.size(), b.size()  <=  10^5
# -10^9  <=  a[i] , b[i]  <=  10^9

# Brute
# T.C. - O(m+n)+O((m+n)log(m+n))+O(m+n)+O(k) ~ O((m+n)log(m+n))
# S.C  - O(m+n)+O(m+n)

# Intuition
# merge two arrays into a list in sorted form
# convert the merged list to set
# convert the set to list and return a ssorted list


class Solution:

    def findUnion(self, a: list[int], b: list[int]) -> list[int]:
        return sorted(list(set(sorted([*a, *b]))))


# Optimal
# T.C. - O(m+n)
# S.C  - O(1)

# Intuition
# just keep track of what you inserted last time
# dont insert if its the same element you inserted last time
# and follow the merge sort algorithm


class Solution:

    def findUnion(self, a: list[int], b: list[int]) -> list[int]:
        union: list[int] = []

        i, j = 0, 0
        last_inserted = (10**9) + 1

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                if last_inserted != a[i]:
                    union.append(a[i])
                    last_inserted = a[i]
                i += 1
            else:
                if last_inserted != b[j]:
                    union.append(b[j])
                    last_inserted = b[j]
                j += 1

        while i < len(a):
            if last_inserted != a[i]:
                union.append(a[i])
                last_inserted = a[i]
            i += 1

        while j < len(b):
            if last_inserted != b[j]:
                union.append(b[j])
                last_inserted = b[j]
            j += 1

        return union
