# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/ , Medium

# Brute
# T.C. -> O(sum(weights)-max(weights))
# S.C. -> O(1)


class Solution:
    def canShip(self, warr, days, maxCapacity):
        cap = 0
        d = 1
        for i in range(len(warr)):
            if cap + warr[i] <= maxCapacity:
                cap += warr[i]
            else:
                d += 1
                cap = warr[i]
        return d <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        for capacity in range(max(weights), sum(weights) + 1):
            if self.canShip(weights, days, capacity):
                return capacity
        return -1


# Optimal
# T.C. -> O(log(sum(weights)-max(weights)))
# S.C. -> O(1)


class Solution:
    def canShip(self, warr, days, maxCapacity):
        cap = 0
        d = 1
        for i in range(len(warr)):
            if cap + warr[i] <= maxCapacity:
                cap += warr[i]
            else:
                d += 1
                cap = warr[i]
        return d <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        st, en = max(weights), sum(weights)

        while st <= en:
            mid = st + (en - st) // 2

            if self.canShip(weights, days, mid):
                en = mid - 1
            else:
                st = mid + 1

        return st
