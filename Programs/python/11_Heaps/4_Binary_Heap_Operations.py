# https://www.geeksforgeeks.org/problems/operations-on-binary-min-heap/1 , Medium


# Optimal
# T.C. - getMin:O(1) insert:O(log(n)) removeMin:O(log(n))
# S.C  - O(n)

"""
heap = [0 for i in range(101)]  # our heap to be used
"""

import math

curr_size = 0
heap = []


def percolate_up(idx):
    if idx > 0:
        pidx = math.ceil((idx / 2) - 1)
        if heap[idx] < heap[pidx]:
            heap[idx], heap[pidx] = heap[pidx], heap[idx]
            percolate_up(pidx)


def percolate_down(idx):
    lc_idx = 2 * idx + 1
    rc_idx = 2 * idx + 2

    smallest_idx = idx

    if lc_idx < curr_size and heap[lc_idx] < heap[idx]:
        smallest_idx = lc_idx

    if rc_idx < curr_size and heap[rc_idx] < heap[smallest_idx]:
        smallest_idx = rc_idx

    if smallest_idx != idx:
        heap[idx], heap[smallest_idx] = (
            heap[smallest_idx],
            heap[idx],
        )
        percolate_down(smallest_idx)


def insertKey(x):
    global curr_size
    global heap

    if curr_size == len(heap):
        heap.append(None)

    heap[curr_size] = x
    percolate_up(curr_size)
    curr_size += 1


def deleteKey(i):
    global curr_size
    if i < 0 or i >= curr_size:
        return -1

    heap[i] = float("-inf")
    percolate_up(i)
    extractMin()


def extractMin():
    global curr_size
    if curr_size == 0:
        return -1

    min_elem = heap[0]
    heap[0] = heap[curr_size - 1]
    curr_size -= 1
    percolate_down(0)
    return min_elem
