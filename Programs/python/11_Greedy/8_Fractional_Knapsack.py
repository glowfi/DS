# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1 , Medium

# Optimal
# T.C. - O(nlog(n))
# S.C  - O(1)

# Selection criteria : Select the weight with highest value/weight ratio


class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        items = []

        for i in range(len(val)):
            items.append([val[i], wt[i]])

        items.sort(key=lambda x: x[0] / x[1], reverse=True)

        max_profit = 0

        for item in items:
            val, wt = item

            if capacity >= wt:
                capacity -= wt
                max_profit += val
            else:
                wt_can_be_taken = capacity / wt
                max_profit += wt_can_be_taken * val
                break  # at this point capacity is less than wt , we take all the possible wt and break and capacity becomes zero

        return max_profit
