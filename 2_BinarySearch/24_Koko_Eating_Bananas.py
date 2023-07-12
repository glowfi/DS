# https://leetcode.com/problems/koko-eating-bananas/ , Medium

# Brute
# T.C. -> O(max(piles)*n)
# S.C. -> O(1)


class Solution(object):
    def getTimeTaken(self, arr, k, h):
        c = 0
        for i in range(len(arr)):
            c += arr[i] // k
            if arr[i] % k != 0:
                c += 1
            if c > h:
                break
        return c

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for i in range(1, max(piles) + 1):
            time = self.getTimeTaken(piles, i, h)
            if time <= h:
                return i
        return -1


# Optimal
# T.C. -> O(log(max(piles))*n)
# S.C. -> O(1)


class Solution:
    def getTimeTaken(self, arr, k, h):
        c = 0
        for i in range(len(arr)):
            c += arr[i] // k
            if arr[i] % k != 0:
                c += 1
            if c > h:
                break
        return c

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        st, en = 1, max(piles)

        while st <= en:
            mid = st + ((en - st) // 2)
            time = self.getTimeTaken(piles, mid, h)

            # Increase number of bananas if time take is more
            if time > h:
                st = mid + 1
            # Else move towards as left as possible as we require minimum no of bananas whick KOKO will able to eat within the given time limit
            else:
                en = mid - 1
        return st
