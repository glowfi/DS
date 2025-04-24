# https://www.geeksforgeeks.org/problems/convert-min-heap-to-max-heap-1666385109/1 , Medium


# Optimal
# T.C. - O(n)
# S.C  - O(n)

import math


class Solution:
    def percolate_down_recursive(self, idx, heap_arr, curr_size):
        lc_idx = 2 * idx + 1
        rc_idx = 2 * idx + 2

        largest_idx = idx

        if lc_idx < curr_size and heap_arr[lc_idx] > heap_arr[idx]:
            largest_idx = lc_idx

        if rc_idx < curr_size and heap_arr[rc_idx] > heap_arr[largest_idx]:
            largest_idx = rc_idx

        if largest_idx != idx:
            heap_arr[idx], heap_arr[largest_idx] = (
                heap_arr[largest_idx],
                heap_arr[idx],
            )
            self.percolate_down_recursive(largest_idx, heap_arr, curr_size)

    def convertMinToMaxHeap(self, N, arr):
        last_internal_node_idx = math.floor(N / 2) - 1

        for i in range(last_internal_node_idx, -1, -1):
            self.percolate_down_recursive(i, arr, N)

        return arr
