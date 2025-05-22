# https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1 , Easy

# Question
# Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it
# into an array of alternate positive and negative numbers without changing the relative order.

# Note:
# - Resulting array should start with a positive integer (0 will also be considered as a positive integer).
# - If any of the positive or negative integers are exhausted, then add the remaining integers in the answer
# as it is by maintaining the relative order.
# - The array may or may not have the equal number of positive and negative integers.

# Examples:

# Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
# Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
# Explanation: The positive numbers are [9, 4, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 4 and then -1 and so on.

# Input: arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# Output: [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
# Explanation : The positive numbers are [5, 2, 4, 7, 1, 8, 0] and the negative integers are [-5,-2,-8]. According to the given conditions we will start from the positive integer 5 and then -5 and so on. After reaching -8 there are no negative elements left, so according to the given rule, we will add the remaining elements (in this case positive elements are remaining) as it in by maintaining the relative order.

# Input: arr[] = [9, 5, -2, -1, 5, 0, -5, -3, 2]
# Output: [9, -2, 5, -1, 5, -5, 0, -3, 2]
# Explanation: The positive numbers are [9, 5, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 5 and then -1 and so on.

# Constraints:
# 1 ≤ arr.size() ≤ 106
# -106 ≤ arr[i] ≤ 106

# Brute
# T.C. - O(N)+O(N) ~ O(N)
# S.C  - O(N)+O(N/2)+O(N/2)

# Intuition
# Separate Positive and Negative numbers
# Merge the Two Vectors Alternately
# After append the remaining elements to the ans


class Solution:
    def rearrange(self, arr: list[int]):
        ans: list[int] = [0 for _ in range(len(arr))]

        pos, neg = [], []

        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        idx = 0
        if len(pos) <= len(neg):
            for i in range(len(pos)):
                ans[idx] = pos[i]
                ans[idx + 1] = neg[i]
                idx += 2
            for j in range(len(pos), len(neg)):
                ans[idx] = neg[j]
                idx += 1
        else:
            for i in range(len(neg)):
                ans[idx] = pos[i]
                ans[idx + 1] = neg[i]
                idx += 2
            for j in range(len(neg), len(pos)):
                ans[idx] = pos[j]
                idx += 1

        arr[::] = ans[::]


# Optimal
# T.C. -
# S.C  -

# Intuition
