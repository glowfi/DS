# https://www.codingninjas.com/studio/problems/k-th-element-of-2-sorted-array_1164159 , Hard


# Brute
# T.C. -> O(n1log(n1))+O(n2log(n2))+O(klog(k))
# S.C. -> O(n)

import heapq


def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    heap = []

    for i in range(len(arr1)):
        heapq.heappush(heap, arr1[i])

    for j in range(len(arr2)):
        heapq.heappush(heap, arr2[j])

    for i in range(k - 1):
        heapq.heappop(heap)

    kele = heapq.heappop(heap)

    return kele


# Optimal
# T.C. -> O()
# S.C. -> O()
