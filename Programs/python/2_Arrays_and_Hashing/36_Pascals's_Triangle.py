# https://leetcode.com/problems/pascals-triangle , Easy

# Question
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


# Constraints:

# 1 <= numRows <= 30

# Brute
# T.C. - O(numRows*last_row)
# S.C  - O(N)

# Intuition
# when starting pad your last seen row with single 0
# For example if a last row is [0,1,2,1,0]
# The next row will be the summation of pairs i,i+1
# [(0+1),(1+2),(2+1),(1+0)] = [1,3,3,1]


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        last_row = [0, 1, 0]

        for i in range(numRows - 1):
            tmp = []
            for j in range(len(last_row) - 1):
                tmp.append(last_row[j] + last_row[j + 1])
            ans.append(tmp)
            last_row = [0, *tmp, 0]

        return ans


# Optimal
# T.C. - O(N^2)
# S.C  - O(1)

# Intuition

# Must Know (1) : Given row and col , find element at row and col , You can find with
# this formula -> row-1 C col-1

# Observation suppose i have 7C2 ->  (7*6)*(5*4*3*2*1)
#                                   -----------------
#                                    (2*1)*(5*4*3*2*1)
# you will see only first 2 in the numerator and denominator is left others get cancel
# try it for others you will see only the "col"(r) part remains
# ------------------------------------------------------------------------------------

# Must Know (2) : Given n print the nth pascals-triangle row, you can use the above
# formula and try to find it in O(N*r) complexity ,but we can improve it a further
# In pascals-triangle the nth row will have n elements
# Given 6th row of pascals-triangle

# Col Idx           0   1        2            3               4                   5

# Observation :     1   5       10           10               5                   1

# Multiplication:   1   5/1    (5*4)/(1*2)  (5*4*3)/(1*2*3) (5*4*3*4)/(1*2*3*4)  (5*4*3*4*5)/(1*2*3*4*5)
#
#
# Formula for finding the ith element in a row  is : (row-col)/col , you just have to maintain previouse cols value
# ------------------------------------------------------------------------------------------------------------------

from typing import List


class Solution:
    def getNRow(self, n: int) -> list[int]:
        ans = 1
        tmp = [1]
        for i in range(1, n):
            ans *= n - i
            ans //= i
            tmp.append(ans)
        return tmp

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            ans.append(self.getNRow(i))

        return ans
