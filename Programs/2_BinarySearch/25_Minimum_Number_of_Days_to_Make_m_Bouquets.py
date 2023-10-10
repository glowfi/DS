# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/ , Medium

# Brute
# T.C. -> O((max(bloomDay)-min(bloomDay)-1)*n)
# S.C. -> O(1)


class Solution:
    def canMake(self, barr, m, k, day):
        count = 0

        for i in range(len(barr)):
            if barr[i] <= day:
                count += 1
            else:
                count = 0

            if count == k:
                count = 0
                m -= 1

            if m == 0:
                return True

        return m == 0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        for day in range(min(bloomDay), max(bloomDay) + 1):
            if self.canMake(bloomDay, m, k, day):
                return day
        return -1


# Optimal
# T.C. -> O(log(max(bloomDay)-min(bloomDay)-1)*n)
# S.C. -> O(1)


class Solution:
    def canMake(self, barr, m, k, day):
        count = 0

        for i in range(len(barr)):
            if barr[i] <= day:
                count += 1
            else:
                count = 0

            if count == k:
                count = 0
                m -= 1

            if m == 0:
                return True

        return m == 0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        st, en = min(bloomDay), max(bloomDay)
        while st <= en:
            mid = st + (en - st) // 2
            if self.canMake(bloomDay, m, k, mid):
                en = mid - 1
            else:
                st = mid + 1
        return st
