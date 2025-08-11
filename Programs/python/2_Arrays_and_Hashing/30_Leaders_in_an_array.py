# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1, Easy, MaintainMinMaxSoFar

# Question
# You are given an array arr of positive integers. Your task is to find all the leaders
# in the array. An element is considered a leader if it is greater than or equal
# to all elements to its right. The rightmost element is always a leader.

# Examples:

# Input: arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

# Input: arr = [10, 4, 2, 4, 1]
# Output: [10, 4, 4, 1]
# Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side

# Input: arr = [5, 10, 20, 40]
# Output: [40]
# Explanation: When an array is sorted in increasing order, only the rightmost element is leader.

# Input: arr = [30, 10, 10, 5]
# Output: [30, 10, 10, 5]
# Explanation: When an array is sorted in non-increasing order, all elements are leaders.

# Constraints:
# 1 <= arr.size() <= 106
# 0 <= arr[i] <= 106


# Optimal
# T.C. - O(N)
# S.C  - O(N)

# Intuition
# traverse the array from right
# keep track of the maximum height from the right till now
# compare the value at current index with the max_from_right so far
# if it is greater then we can say its a leader


class Solution:
    def leaders(self, arr: list[int]) -> list[int]:
        max_from_right = arr[-1]

        n = len(arr)
        ans = [arr[-1]]

        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                ans.append(arr[i])
                max_from_right = arr[i]

        return ans[::-1]
