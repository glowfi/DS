# https://www.geeksforgeeks.org/problems/square-root/1 , Easy

# Question
# Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.

# Floor value of any number is the greatest Integer which is less than or equal to that number

# Examples:

# Input: n = 4
# Output: 2
# Explanation: Since, 4 is a perfect square, so its square root is 2.

# Input: n = 11
# Output: 3
# Explanation: Since, 11 is not a perfect square, floor of square root of 11 is 3.

# Input: n = 1
# Output: 1

# Constraints:
# 1 ≤ n ≤ 3*10^4

# Brute
# T.C. - O(N)
# S.C  - O(1)

# Intuition
# Just keep checking if we square the number
# starting from 1 to n and we get back the
# input number then return the i , if we
# exceed the number then we exit out of the loop
# Also keep track of the number as we iterate


class Solution:
    def floorSqrt(self, n: int) -> int:
        ans = 1
        for i in range(1, n + 1):
            if i * i == n:
                return i
            if i * i > n:
                break
            ans = i

        return ans


# Optimal
# T.C. - O(log(N))
# S.C  - O(1)

# Intuition
# start a binary search with start
# as 1 and end as number just keep
# checking if we square the number and
# exceed then we move more towards left
# and if we are less then number we move
# towards right increasing our search space
# if we see the square of current mid equals
# the original number we return


class Solution:
    def floorSqrt(self, n: int) -> int:
        st, en = 1, n + 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if mid * mid == n:
                return mid

            if mid * mid < n:
                st = mid + 1
                ans = mid
            else:
                en = mid - 1

        return ans
