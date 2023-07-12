# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/ , Medium

# Brute
# T.C. -> O(sum(weights)-max(weights))
# S.C. -> O(1)


class Solution:
    def canShip(self, arr, currCap, days):
        quota = 0
        d = 1
        for i in range(len(arr)):
            if quota + arr[i] > currCap:
                d += 1
                quota = arr[i]
            else:
                quota += arr[i]

        return d <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        for i in range(max(weights), sum(weights) + 1):
            if self.canShip(weights, i, days):
                return i
        return -1


# Optimal
# T.C. -> O(log(sum(weights)-max(weights)))
# S.C. -> O(1)


class Solution:
    def canShip(self, arr, currCap, days):
        quota = 0
        d = 1
        for i in range(len(arr)):
            if quota + arr[i] > currCap:
                d += 1
                quota = arr[i]
            else:
                quota += arr[i]

        return d <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        st, en = max(weights), sum(weights)

        while st <= en:
            mid = st + ((en - st) // 2)

            if self.canShip(weights, mid, days):
                en = mid - 1
            else:
                st = mid + 1
        return st
