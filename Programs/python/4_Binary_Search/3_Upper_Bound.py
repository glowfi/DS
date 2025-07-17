# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1 , Easy

# Question
# Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

# Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
# Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

# Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present.

# Examples:

# Input: x = 7 , arr[] = [5, 6, 8, 9, 6, 5, 5, 6]
# Output: 6, 8
# Explanation: Floor of 7 is 6 and ceil of 7 is 8.

# Input: x = 10 , arr[] = [5, 6, 8, 8, 6, 5, 5, 6]
# Output: 8, -1
# Explanation: Floor of 10 is 8 but ceil of 10 is not possible.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints :
# 1 ≤ arr.size ≤ 10^5
# 1 ≤ arr[i], x ≤ 10^6


# Optimal
# T.C. - O(log(N))+O(log(N)) ~ O(log(N))
# S.C  - O(1)

# Intuition
# Do a binary search for floor
# since we need to find the value lesser than equal to x but the largest
# when we encounter an element with that condition we store the index
# in an answer and move more towards right and if we find number greater
# than target we move towards left
#
# Do a binary search for ceil
# since we need to find the value greater than equal to x but the smallest
# when we encounter an element with that condition we store the index
# in an answer and move more towards left and if we find number lesser
# than target we move towards right


class Solution:
    def floor(self, x: int, arr: list[int]):
        st, en = 0, len(arr) - 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if arr[mid] <= x:
                ans = arr[mid]
                st = mid + 1
            elif arr[mid] > x:
                en = mid - 1

        return ans

    def ceil(self, x: int, arr: list[int]):
        st, en = 0, len(arr) - 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if arr[mid] >= x:
                ans = arr[mid]
                en = mid - 1
            else:
                st = mid + 1

        return ans

    def getFloorAndCeil(self, x: int, arr: list[int]) -> list[int]:
        arr.sort()
        floor = self.floor(x, arr)
        ceil = self.ceil(x, arr)

        return [floor, ceil]
