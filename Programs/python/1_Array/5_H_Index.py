# https://leetcode.com/problems/h-index, Medium, Counting Sort

# Question
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1

# Brute
# T.C. - O(max(citations)*n)+O(nlog(n))
# S.C  - O(1)

# Intuition
# For all possible values of citations
# check whether we can find alteast x papers with x
# no of citations

from typing import List


class Solution:
    def hasAtleast_H_Paper_With_H_Citation(self, h: int, citations: List[int]):
        paper_with_h_citations = 0
        for citation_val in citations:
            if citation_val >= h:
                paper_with_h_citations += 1

        return True if paper_with_h_citations >= h else False

    def hIndex(self, citations: List[int]) -> int:
        h_idx = 0
        citations.sort()

        for h_index in range(max(citations) + 1):
            if self.hasAtleast_H_Paper_With_H_Citation(h_index, citations):
                h_idx = h_index

        return h_idx


# Better
# T.C. - O(nlog(n))
# S.C  - O(1)

# Intuition
# We are going to do a binary search in the range
# of 1 and max value of citaion
# if for current value of h_index we are able to
# find h paper with h citations we are going to
# go towards right otherwise to the left

from typing import List


class Solution:
    def hasAtleast_H_Paper_With_H_Citation(self, h: int, citations: List[int]):
        paper_with_h_citations = 0
        for citation_val in citations:
            if citation_val >= h:
                paper_with_h_citations += 1

        return True if paper_with_h_citations >= h else False

    def hIndex(self, citations: List[int]) -> int:
        h_idx = 0
        citations.sort()
        st, en = 0, max(citations) + 1

        while st <= en:
            mid = (st + en) // 2

            if self.hasAtleast_H_Paper_With_H_Citation(mid, citations):
                h_idx = mid
                st = mid + 1
            else:
                en = mid - 1

        return h_idx


# Optimal
# T.C. - O(n)
# S.C  - O(n)

# Intuition
# We are going to follow a counting sort appraoch
# We are going to initialize a count array of size n+1
# In that count array we are going to store how many
# times ith citations value has occured
# Rememeber the count array stores the paper count with
# exactly i as the h-index not how many papers with atlest h-index
# Then we are going to traverse back from the array and maintain
# paper count we have seen so far. For every index we are going to
# ask one question does we have atleast h paper with h citation
# if yes we return the first value we get

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # count[i] = how many papers have exactly i citations (i from 0..n)
        count = [0] * (n + 1)

        for c in citations:
            # citations larger than n are capped at n
            count[min(c, n)] += 1

        paper = 0  # number of papers with citations >= current i
        for i in range(n, -1, -1):
            paper += count[i]  # add papers that have i citations
            if paper >= i:  # H‑index condition satisfied
                return i
        return 0
