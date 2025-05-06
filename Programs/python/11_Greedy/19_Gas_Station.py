# https://leetcode.com/problems/gas-station , Medium

# Brute
# T.C. - O(n^2)
# S.C  - O(1)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for idx, g in enumerate(gas):
            if g - cost[idx] < 0:
                continue

            curr_gas_cap = g - cost[idx]
            j = (idx + 1) % len(gas)
            canComplete = True

            while j != idx:
                if curr_gas_cap + gas[j] - cost[j] < 0:
                    canComplete = False
                    break
                curr_gas_cap = (curr_gas_cap + gas[j]) - cost[j]
                j = (j + 1) % len(gas)

            if canComplete:
                return idx

        return -1


# Optimal
# T.C. - O(n)
# S.C  - O(1)

# Intuition
# + The first step is to check whether the total amount of gas available is sufficient to cover the total cost of traveling to all gas stations.
# During the iteration, if the net gas difference total at any point becomes negative,
# it indicates that the current starting station cannot complete the circuit. In such cases, we reset the total to
# zero and update the starting index res to the next station.
# At the end of traversal, if the net gas difference total remains non-negative, it
# signifies that there exists a starting station from which we can complete the circuit without running out of gas.


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        res = 0
        gas_cap = 0

        for i in range(len(gas)):
            gas_cap += gas[i] - cost[i]

            if gas_cap < 0:
                gas_cap = 0
                res = i + 1

        return res
