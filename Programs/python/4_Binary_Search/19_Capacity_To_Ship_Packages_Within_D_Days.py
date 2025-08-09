# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days , Medium, BS-on-Ans

# Question
# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.


# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
# Example 2:

# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# Example 3:

# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1


# Constraints:

# 1 <= days <= weights.length <= 5 * 10^4
# 1 <= weights[i] <= 500

# Brute
# T.C. - O(sum(weights)*N)+O(N)+O(N)
# S.C  - O(1)

# Intuition
# we start a linear search starting
# with starting weight as max in given weights array and ending
# weight as sum of all the weights,the first time
# we see we are able to ship within the given days d
# we return the current capacity


from typing import List


class Solution:
    def canShip(self, weights: List[int], days: int, maxCap: int) -> bool:
        daysTaken = 0
        currCap = maxCap

        for i in range(len(weights)):
            if currCap == 0:
                daysTaken += 1
                currCap = maxCap

            if weights[i] <= currCap:
                currCap -= weights[i]
            else:
                daysTaken += 1
                currCap = maxCap
                currCap -= weights[i]

        if currCap <= maxCap:
            daysTaken += 1

        return daysTaken <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        for currCap in range(max(weights), sum(weights) + 1):
            if self.canShip(weights, days, currCap):
                return currCap
        return -1


# Optimal
# T.C. - O(log(sum(weights))*N)+O(N)+O(N)
# S.C  - O(1)

# Intuition
# We start a binary a binary search
# with starting weight as max in given weights array and ending
# weight as sum of all the weights,we
# check if we are able to ship within
# the given time d with the current weight
# max capacity we move to left with the motive
# to minimize capacity,otherwise we go to right

from typing import List


class Solution:
    def canShip(self, weights: List[int], days: int, maxCap: int) -> bool:
        daysTaken = 0
        currCap = maxCap

        for i in range(len(weights)):
            if currCap == 0:
                daysTaken += 1
                currCap = maxCap

            if weights[i] <= currCap:
                currCap -= weights[i]
            else:
                daysTaken += 1
                currCap = maxCap
                currCap -= weights[i]

        if currCap <= maxCap:
            daysTaken += 1

        return daysTaken <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        st, en = max(weights), sum(weights) + 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if self.canShip(weights, days, mid):
                ans = mid
                en = mid - 1
            else:
                st = mid + 1

        return ans
