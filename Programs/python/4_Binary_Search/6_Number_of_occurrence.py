# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1, Easy, floor/ceil

# Question
# Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[].

# Examples :

# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
# Output: 4
# Explanation: target = 2 occurs 4 times in the given array so the output is 4.

# Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
# Output: 0
# Explanation: target = 4 is not present in the given array so the output is 0.

# Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
# Output: 3
# Explanation: target = 12 occurs 3 times in the given array so the output is 3.

# Constraints:
# 1 ≤ arr.size() ≤ 10^6
# 1 ≤ arr[i] ≤ 10^6
# 1 ≤ target ≤ 10^6


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# Find first occurence (F)
# Find last occurence (L)
# return L-F+1


from typing import List


class Solution:
    def firstOccurence(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                ans = mid
                en = mid - 1

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return ans

    def lastOccurence(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        st, en = 0, len(nums) - 1

        while st <= en:
            mid = st + (en - st) // 2

            if nums[mid] == target:
                ans = mid
                st = mid + 1

            elif nums[mid] < target:
                st = mid + 1

            elif nums[mid] > target:
                en = mid - 1

        return ans

    def countFreq(self, arr: list[int], target: int):
        lastOccurence = self.lastOccurence(arr, target)
        firstOccurence = self.firstOccurence(arr, target)
        if lastOccurence == len(arr) and firstOccurence == len(arr):
            return 0
        return (lastOccurence - firstOccurence) + 1
