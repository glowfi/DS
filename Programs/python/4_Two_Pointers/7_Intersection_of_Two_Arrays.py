# https://leetcode.com/problems/intersection-of-two-arrays, Easy, Two Pointers

# Question
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# Brute
# T.C. - O(mlog(m))+O(nlog(n))+O(m+n)
# S.C  - O(m+n)+O(m+n)

# Intuition
# Sort the array
# Take 2 pointers p1 and p2 pointing to start indexes of 2 arrays
# If elements at p1 and p2 are equal add it to resultant set
# otherwise increment the pointer that points to the smaller
# integer value

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        res = set()
        p1, p2 = 0, 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.add(nums1[p1])
                p1 += 1
                p2 += 1
            else:
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1

        return list(res)


# Better
# T.C. - O(m+n)
# S.C  - O(m)+O(m+n)

# Intuition
# Take 2 visited maps for nums1 and nums2
# Put all the elements of nums1 in a visited map 1
# Traverse the second array nums2 only if it is
# present in first visted map and not in visited map 2
# put it in the result array

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited1 = {}
        res = []

        for num in nums1:
            visited1[num] = 1

        visited2 = {}
        for num in nums2:
            if num in visited1 and num not in visited2:
                res.append(num)
            visited2[num] = 1

        return res


# Optimal
# T.C. - O(m+n)
# S.C  - O(m+n)

# Intuition
# Take 1 visited map for nums1.
# Put all the elements of nums1 in a visited map 1
# Traverse the second array nums2 only if it is
# present in visited map 1 the put it in the result
# array and delete the record from visted map 1 as
# we dont want to add duplicateson result array


from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited = {}
        res = []

        for num in nums1:
            visited[num] = 1

        for num in nums2:
            if num in visited:
                del visited[num]
                res.append(num)

        return res
