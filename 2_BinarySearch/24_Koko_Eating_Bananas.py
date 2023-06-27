# https://leetcode.com/problems/koko-eating-bananas/ , Medium

# Brute
# T.C. -> O(max(piles)*n)
# S.C. -> O(1)


class Solution:
    def getHours(self, speed, piles, h):
        c = 0
        for i in piles:
            c += i // speed
            if i % speed != 0:
                c += 1
            if c > h:
                break
        return c

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1

        while True:
            time = self.getHours(k, piles, h)
            if time > h:
                k += 1
            else:
                return k


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


class Solution(object):
    def getHours(self, speed, piles, h):
        c = 0
        for i in piles:
            c += i // speed
            if i % speed != 0:
                c += 1
            if c > h:
                break
        return c

    def minEatingSpeed(self, piles, h):
        st, en = 1, max(piles)

        while st <= en:
            mid = st + (en - st) // 2

            if self.getHours(mid, piles, h) <= h:
                en = mid - 1
            else:
                st = mid + 1
        return st
