# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets , Medium

# Question
# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


# Example 1:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
# Example 2:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
# Example 3:

# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here is the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.


# Constraints:

# bloomDay.length == n
# 1 <= n <= 10^5
# 1 <= bloomDay[i] <= 10^9
# 1 <= m <= 10^6
# 1 <= k <= n

# Brute
# T.C. - O(max(bloomDay)*N)+O(N)
# S.C  - O(1)

# Intuition
# we start with a day range starting from
# 1 and ending at max of days taken to bloom
# from given bloomDay array.We start a linear
# search, the first time we see that with our
# current day we are able to make m bouquet with
# k adjacent flowers we return the current day


from typing import List


class Solution:
    def canMakeBouquet(self, bloomDay: List[int], currDay: int, m: int, k: int) -> bool:
        tmp = k
        c = 0

        for i in range(len(bloomDay)):
            if tmp == 0:
                c += 1
                tmp = k

            if bloomDay[i] > currDay:
                tmp = k

            if bloomDay[i] <= currDay:
                tmp -= 1

        if tmp == 0:
            c += 1

        return c >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        for i in range(1, max(bloomDay) + 1):
            if self.canMakeBouquet(bloomDay, i, m, k):
                return i
        return -1


# Optimal
# T.C. - O(log(max(bloomDay))*N)+O(N)
# S.C  - O(1)

# Intuition
# we start with a day range starting from
# 1 and ending at max of days taken to bloom
# from given bloomDay array.We start a binary
# search, if we are able to make m bouquet with
# k adjacent flowers with the current day we move
# to the left with our motive being to minimze the
# number of days, otherwise we move to the right


from typing import List


class Solution:
    def canMakeBouquet(self, bloomDay: List[int], currDay: int, m: int, k: int) -> bool:
        tmp = k
        c = 0

        for i in range(len(bloomDay)):
            if tmp == 0:
                c += 1
                tmp = k

            if bloomDay[i] > currDay:
                tmp = k

            if bloomDay[i] <= currDay:
                tmp -= 1

        if tmp == 0:
            c += 1

        return c >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        st, en = 1, max(bloomDay) + 1
        ans = -1

        while st <= en:
            mid = st + (en - st) // 2

            if self.canMakeBouquet(bloomDay, mid, m, k):
                ans = mid
                en = mid - 1
            else:
                st = mid + 1

        return ans
