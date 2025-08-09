# https://leetcode.com/problems/h-index , Medium, CountSort

# Question
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper,
# return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the
# maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.


# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1


# Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

# Brute
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition
# Do i have h papers that has been cited h times
# start with 0 and keep increasing the index by 1
# and check if there can be h-index of i
# sice we have an array of size n, the max h-index
# can be n


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0

        for i in range(1, len(citations) + 1):
            c = 0
            for j in range(len(citations)):
                if citations[j] >= i:
                    c += 1
                if c == i:
                    h_index = i
                    break

        return h_index


# Optimal
# T.C. - O(N)+O(N) ~ O(N)
# S.C  - O(N)

# Intuition
# we use a counting sort techique to solve this problem
# first we create an array of size n+1
# each index in the array represents the count of paper having i citaions
# since we can have citations more than size of the array for those cases
# we are going to use the last index of the array to store count
# we start iterating from back of the array and check whether we have
# papers more than i value or not if we have then we just return i


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count_arr = [0] * (len(citations) + 1)

        for i in range(len(citations)):
            if citations[i] >= len(citations):
                count_arr[len(citations)] += 1
            else:
                count_arr[citations[i]] += 1

        paper_count = 0
        for i in range(len(count_arr) - 1, -1, -1):
            paper_count += count_arr[i]
            if paper_count >= i:
                return i

        return 0
