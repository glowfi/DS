# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/ , Medium

# Brute
# T.C. -> O(max(bloomDay)*n)
# S.C. -> O(1)

from typing import *


class Solution:
    def canCompleteBouquet(self, day, m, k, arr):
        c = 0
        bouq = 0
        for i in range(len(arr)):
            if arr[i] <= day:
                c += 1
            else:
                bouq += c // k
                c = 0
            if bouq >= m:
                return True
        bouq += c // k
        if bouq >= m:
            return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        day = min(bloomDay)

        if (m * k) > len(bloomDay):
            return -1

        while day <= max(bloomDay):
            if self.canCompleteBouquet(day, m, k, bloomDay):
                return day
            day += 1
        return -1


# Optimal
# T.C. -> O(log(max-min-1)*n)
# S.C. -> O(1)


class Solution:
    def canCompleteBouquet(self, day, m, k, arr):
        c = 0
        bouq = 0
        for i in range(len(arr)):
            if arr[i] <= day:
                c += 1
            else:
                bouq += c // k
                c = 0
            if bouq >= m:
                return 1
        bouq += c // k
        if bouq >= m:
            return 1
        return 0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (m * k) > len(bloomDay):
            return -1

        st, en = min(bloomDay), max(bloomDay)

        while st <= en:
            mid = (st + en) // 2

            if self.canCompleteBouquet(mid, m, k, bloomDay) == 1:
                en = mid - 1
            else:
                st = mid + 1
        return st
