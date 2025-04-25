# https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1 , Easy


# Optimal
# T.C. - O(N*denominations*coin_selected)
# S.C  - O(1)

# Selection criteria : Select the highest denominations first to reduce the value of N quickly as we need to choose min coins


class Solution:
    def minPartition(self, N):
        denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

        ans = []

        while N:
            for denomination in denominations:
                coin_selected = N // denomination
                for num in range(coin_selected):
                    ans.append(denomination)
                    N -= denomination

        return ans
