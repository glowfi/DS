# https://leetcode.com/problems/total-cost-to-hire-k-workers , Medium

# Better
# T.C. - O(k⋅logm)  m is candidates,k is no of hiring rounds
# S.C  - O(m)+O(m)

import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        h1, h2 = [], []
        total_cost = 0
        i, j = 0, len(costs) - 1

        while k:
            while i <= j and len(h1) < candidates:
                heapq.heappush(h1, costs[i])
                i += 1

            while j >= i and len(h2) < candidates:
                heapq.heappush(h2, costs[j])
                j -= 1

            top_h1 = h1[0] if h1 else float("inf")
            top_h2 = h2[0] if h2 else float("inf")

            if top_h1 <= top_h2:
                total_cost += heapq.heappop(h1)
            else:
                total_cost += heapq.heappop(h2)

            k -= 1

        return total_cost


# Optimal
# T.C. - O(k⋅logm)  m is candidates,k is no of hiring rounds
# S.C  - O(m)

import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        h = []
        total_cost = 0
        i, j = 0, len(costs) - 1
        push_ops_i_count = 0
        push_ops_j_count = 0

        while k:

            while i <= j and push_ops_i_count < candidates:
                heapq.heappush(h, [costs[i], i, 0])
                push_ops_i_count += 1
                i += 1

            while j >= i and push_ops_j_count < candidates:
                heapq.heappush(h, [costs[j], j, 1])
                push_ops_j_count += 1
                j -= 1

            cost, _, came_from = heapq.heappop(h)
            if came_from == 0:
                push_ops_i_count -= 1
            else:
                push_ops_j_count -= 1
            total_cost += cost

            k -= 1

        return total_cost
