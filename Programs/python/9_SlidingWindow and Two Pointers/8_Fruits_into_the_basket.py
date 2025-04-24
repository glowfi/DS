# https://leetcode.com/problems/fruit-into-baskets/ , Medium

# Brute
# T.C. - O(N^2)
# S.C  - O(n)


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        hmap = {}
        k = 2
        mx_fruits = float("-inf")

        for i in range(n):
            c = 0
            for j in range(i, n):
                if fruits[j] not in hmap:
                    hmap[fruits[j]] = 1
                else:
                    hmap[fruits[j]] += 1
                if len(hmap) > k:
                    hmap = {}
                    break
                c += 1
                mx_fruits = max(mx_fruits, c)

        return mx_fruits


# Better
# T.C. - O(2n)
# S.C  - O(n)


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        n = len(fruits)
        hmap = {}
        k = 2
        mx_fruits = float("-inf")

        while r < n:
            currFruit = fruits[r]
            if fruits[r] not in hmap:
                hmap[currFruit] = 1
            else:
                hmap[currFruit] += 1

            while len(hmap) > k:
                if hmap[fruits[l]] - 1 == 0:
                    del hmap[fruits[l]]
                else:
                    hmap[fruits[l]] -= 1
                l += 1

            if len(hmap) <= k:
                mx_fruits = max(mx_fruits, r - l + 1)

            r += 1

        return mx_fruits


# Optimal
# T.C. - O(n)
# S.C  - O(n)


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        n = len(fruits)
        hmap = {}
        k = 2
        mx_fruits = float("-inf")

        while r < n:
            currFruit = fruits[r]
            if fruits[r] not in hmap:
                hmap[currFruit] = 1
            else:
                hmap[currFruit] += 1

            if len(hmap) > k:
                if hmap[fruits[l]] - 1 == 0:
                    del hmap[fruits[l]]
                else:
                    hmap[fruits[l]] -= 1
                l += 1

            if len(hmap) <= k:
                mx_fruits = max(mx_fruits, r - l + 1)

            r += 1

        return mx_fruits
