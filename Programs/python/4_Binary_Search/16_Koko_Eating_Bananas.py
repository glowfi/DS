# https://leetcode.com/problems/koko-eating-bananas, Medium, BS-on-Ans

# Question
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


# Constraints:

# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9

# Brute
# T.C. - O(max(piles)*N)+O(N)
# S.C  - O(1)

# Intuition
# We start a loop from start index as 1 and end index
# as the max number of bananas in the pile,the first
# time we encounter a speed with which we are able to
# eat all the bananas within given time h we return the
# speed

import math
from typing import List


class Solution:
    def timeTakenToEat(self, piles: List[int], curr_speed: int) -> int:
        time = 0

        for pile in piles:
            time += math.ceil(pile / curr_speed)

        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for i in range(1, max(piles) + 1):
            if self.timeTakenToEat(piles, i) <= h:
                return i
        return -1


# Optimal
# T.C. - O(log(max(piles))*N)+O(N)
# S.C  - O(1)

# Intuition
# We choose a starting min speed from 1 and max speed
# with max bananas in the pile,with the current speed
# we check if its possible to eat all bananas within
# the given time,if time taken in more than h we move
# more towards right increasing our speed otherwise
# we move more towards the left if we can eat bannana
# with the curr_speed with motive being to minimize
# our speed and still able to eat all bananas

import math
from typing import List


class Solution:
    def timeTakenToEat(self, piles: List[int], curr_speed: int) -> int:
        time = 0

        for pile in piles:
            time += math.ceil(pile / curr_speed)

        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        st, en = 1, max(piles) + 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            t = self.timeTakenToEat(piles, mid)

            if t <= h:
                ans = mid
                en = mid - 1
            else:
                st = mid + 1

        return ans
