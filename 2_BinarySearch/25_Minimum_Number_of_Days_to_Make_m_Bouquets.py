# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/ , Medium

# Brute
# T.C. -> O((max(bloomDay)-min(bloomDay)-1)*n)
# S.C. -> O(1)


class Solution:
    def canMake(self, arr, m, k, currDay):
        ad = 0
        bouq = 0
        for i in range(len(arr)):
            if arr[i] <= currDay:
                ad += 1

            elif arr[i] > currDay:
                ad = 0

            if ad == k:
                ad = 0
                bouq += 1

            if bouq == m:
                return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        for i in range(min(bloomDay), max(bloomDay) + 1):
            if self.canMake(bloomDay, m, k, i):
                return i

        return -1


# Optimal
# T.C. -> O(log(max(bloomDay)-min(bloomDay)-1)*n)
# S.C. -> O(1)


class Solution:
    def canMake(self, arr, m, k, currDay):
        ad = 0
        bouq = 0
        for i in range(len(arr)):
            if arr[i] <= currDay:
                ad += 1

            elif arr[i] > currDay:
                ad = 0

            if ad == k:
                ad = 0
                bouq += 1

            if bouq == m:
                return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        st, en = min(bloomDay), max(bloomDay)

        while st <= en:
            mid = st + ((en - st) // 2)

            if self.canMake(bloomDay, m, k, mid):
                en = mid - 1
            else:
                st = mid + 1

        return st
