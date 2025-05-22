# https://www.geeksforgeeks.org/problems/counting-sort/1 , Easy

# Question
# Given a string arr consisting of lowercase english letters, arrange all its letters in lexicographical order using Counting Sort.

# Example 1:

# Input:
# N = 5
# S = "edsab"
# Output:
# abdes
# Explanation:
# In lexicographical order, string will be
# abdes.
# Example 2:

# Input:
# N = 13
# S = "geeksforgeeks"
# Output:
# eeeefggkkorss
# Explanation:
# In lexicographical order, string will be
# eeeefggkkorss.
# Your Task:
# This is a function problem. You only need to complete the function countSort() that takes string arr as a parameter and returns the sorted string. The printing is done by the driver code.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 ≤ N ≤ 10^5


# Optimal
# T.C. - O(N+26)
# S.C  - O(26)+O(N)

# Intuition
# This is a non comparison basesd algo
# This algo work best when all input elements are within a given range k.
# This algorithms avg,best,worst time complexity is O(Nlog(N)) and worst case
# This is a unstable sorting algo.
# create a count array of size either max element+1 or given k+1
# store the frequence of each element in the count array
# then replace everything in the count array with prefix sum
# such that count[i]=count[i]+count[i-1]
# loop from back of the input array suppose we enconter number 2
# in our input array then we go to the index 2 in the count array
# the value at that index 2 will gives us where to place 2 in the final output array
# decrement count of 2 in the count array
# place the 2 in that index postion got from count array


class Solution:
    def countSort(self, arr: list[str]):
        count_arr = [0] * 27

        # calculate frequency
        for char in arr:
            count_arr[ord(char) - 97] += 1

        # calculate prefix sum
        for i in range(1, len(count_arr)):
            count_arr[i] = count_arr[i] + count_arr[i - 1]

        # build output array
        out = [""] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            num = ord(arr[i]) - 97
            count_arr[num] -= 1
            out[count_arr[num]] = arr[i]

        return "".join(out)
