# https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1, Medium, BS-on-Ans

# Question
# You are given 2 numbers n and m, the task is to find n√m (nth root of m). If the root is not integer then returns -1.

# Examples :

# Input: n = 2, m = 9
# Output: 3
# Explanation: 32 = 9

# Input: n = 3, m = 9
# Output: -1
# Explanation: 3rd root of 9 is not integer.

# Input: n = 1, m = 14
# Output: 14

# Constraints:
# 1 <= n <= 30
# 1 <= m <= 10^9

# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just keep checking if number to the pow n
# starting from 1 to n and we get back the
# input number then return the i , if we
# exceed the number then we exit out of the loop


class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        for i in range(1, m + 1):
            if i**n == m:
                return i

        return -1


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# start a binary search with start
# as 1 and end as number just keep
# checking if we number to the pow n and
# exceed then we move more towards left
# and if we are less then number we move
# towards right increasing our search space
# if we see the number to the pow n of current mid equals
# the original number we return


class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        st, en = 1, m + 1

        while st <= en:
            mid = st + (en - st) // 2

            if mid**n == m:
                return mid

            if mid**n < m:
                st = mid + 1
            else:
                en = mid - 1

        return -1
