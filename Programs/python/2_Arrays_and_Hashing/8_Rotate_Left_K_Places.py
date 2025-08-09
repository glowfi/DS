# https://practice.geeksforgeeks.org/problems/reversal-algorithm5340/1 , Easy, Rotation

# Question
# Given an array arr[]. The task is to rotate the array by d elements where d ≤ arr.size.

# Examples:

# Input: arr[] = [-1, -2, -3, 4, 5, 6, 7], d = 2
# Output: [-3, 4, 5, 6, 7, -1, -2]
# Explanation:
# Rotate by 1: [-2, -3, 4, 5, 6, 7, -1]
# Rotate by 2: [-3, 4, 5, 6, 7, -1, -2]

# Input: arr[] = [1, 3, 4, 2], d = 3
# Output: [2, 1, 3, 4]
# Explanation: After rotating the array three times, the first three elements shift one by one to the right.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ arr.size ≤ 10^6
# -10^9 ≤ arr[i] ≤ 10^9
# 0 ≤ d ≤ arr.size

# Brute
# T.C. - O(d*N)
# S.C  - O(1)

# Intuition
# keep left rotating by one place for d times


class Solution:
    def rotate(self, arr: list[int]):
        for i in range(len(arr) - 1):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    def leftRotate(self, arr: list[int], d: int) -> None:
        while d:
            self.rotate(arr)
            d -= 1


# Optimal
# T.C. - O(k)+O(N-k)+O(N)
# S.C  - O(1)

# Intuition
# reverse the array from 0 to k-1
# reverse the array from k to len(arr)-1
# reverse the whole array


class Solution:
    def leftRotate(self, arr: list[int], d: int) -> None:

        def rev_array(arr: list[int], i: int, j: int) -> None:
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        rev_array(arr, 0, d - 1)
        rev_array(arr, d, len(arr) - 1)
        rev_array(arr, 0, len(arr) - 1)
