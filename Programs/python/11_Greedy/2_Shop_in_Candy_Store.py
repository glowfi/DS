# https://www.geeksforgeeks.org/problems/shop-in-candy-store1145/1 , Easy


# Optimal
# T.C. - 2*O(nlog(n))+2*O(n)
# S.C  - o(2)

# Selection criteria : For min cost choose the min values first, For max cost choose the max values first


class Solution:

    def candyStore(self, candies, N, K):
        # handle min
        min_cost = 0
        candies.sort()
        i, j = 0, len(candies) - 1

        while i <= j:
            min_cost += candies[i]
            i += 1
            c = K
            while c:
                c -= 1
                j -= 1

        # handle max
        max_cost = 0
        candies.sort(reverse=True)
        i, j = 0, len(candies) - 1

        while i <= j:
            max_cost += candies[i]
            i += 1
            c = K
            while c:
                c -= 1
                j -= 1

        return [min_cost, max_cost]
