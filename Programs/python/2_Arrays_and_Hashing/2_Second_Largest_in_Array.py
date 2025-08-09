# https://practice.geeksforgeeks.org/problems/second-largest3735/1 , Easy, Basic

# Question
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.

# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

# Constraints:
# 2 ≤ arr.size() ≤ 10^5
# 1 ≤ arr[i] ≤ 10^5


# Better
# T.C. - O(N)+O(N) ~ O(N)
# S.C  - O(1)

# Intuition
# first find the largest
# then again find the largest excluding already found largest value


class Solution:
    def getSecondLargest(self, arr: list[int]) -> int:
        largest = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > largest:
                largest = arr[i]

        sec_largest = -1
        for j in range(len(arr)):
            if arr[j] != largest and arr[j] > sec_largest:
                sec_largest = arr[j]

        return sec_largest


# Optimal
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# in one pass we try to find max and sec_largest
# by utilizing 2 condition
# + if current element is greater than sec_largest,but smaller than largest
# + if current element is greater than largest


class Solution:
    def getSecondLargest(self, arr: list[int]) -> int:
        largest = arr[0]
        sec_largest = -1

        for i in range(1, len(arr)):
            if arr[i] < largest and arr[i] > sec_largest:
                sec_largest = arr[i]

            if arr[i] > largest:
                sec_largest = largest
                largest = arr[i]

        return sec_largest
