# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1 , Easy

# Question
# Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x. This element is called the floor of x. If such an element does not exist, return -1.

# Note: In case of multiple occurrences of ceil of x, return the index of the last occurrence.

# Examples

# Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
# Output: 1
# Explanation: Largest number less than or equal to 5 is 2, whose index is 1.

# Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 11
# Output: 4
# Explanation: Largest Number less than or equal to 11 is 10, whose indices are 3 and 4. The index of last occurrence is 4.

# Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 0
# Output: -1
# Explanation: No element less than or equal to 0 is found. So, output is -1.

# Constraints:
# 1 ≤ arr.size() ≤ 10^6
# 1 ≤ arr[i] ≤ 10^6
# 0 ≤ x ≤ arr[n-1]


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Do a binary search for floor
# since we need to find the value lesser than equal to x but the largest
# when we encounter an element with that condition we store the index
# in an answer and move more towards right and if we find number greater
# than target we move towards left


class Solution:
    def findFloor(self, arr: list[int], x: int) -> int:
        st, en = 0, len(arr) - 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if arr[mid] <= x:
                ans = mid
                st = mid + 1
            elif arr[mid] > x:
                en = mid - 1

        return ans
