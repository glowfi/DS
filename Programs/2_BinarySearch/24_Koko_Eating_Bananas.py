# https://leetcode.com/problems/koko-eating-bananas/ , Medium

# Brute
# T.C. -> O(max(piles)*n)
# S.C. -> O(1)


class Solution:
    def canEat(self, k, arr, h):
        timeTaken = 0
        for i in range(len(arr)):
            timeTaken = arr[i] // k
            if arr[i] % k != 0:
                timeTaken += 1
            h -= timeTaken
            if h < 0:
                return False
        return h >= 0

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for speed in range(1, max(piles) + 1):
            if self.canEat(speed, piles, h):
                return speed
        return -1


# Optimal
# T.C. -> O(log(max(piles))*n)
# S.C. -> O(1)


class Solution:
    def canEat(self, k, arr, h):
        timeTaken = 0
        for i in range(len(arr)):
            timeTaken = arr[i] // k
            if arr[i] % k != 0:
                timeTaken += 1
            h -= timeTaken
            if h < 0:
                return False
        return h >= 0

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        st, en = 1, max(piles)

        while st <= en:
            mid = st + (en - st) // 2

            if self.canEat(mid, piles, h):
                en = mid - 1
            else:
                st = mid + 1
        return st
