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


# Better
# T.C. -> O(n+m)
# S.C. -> O(1)


def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    c = 1
    ans = -1

    i, j = 0, 0
    n1, n2 = len(arr1), len(arr2)

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if c == k:
                ans = arr1[i]
            c += 1
            i += 1
        else:
            if c == k:
                ans = arr2[j]

            c += 1
            j += 1

    while i < n1:
        if c == k:
            ans = arr1[i]
        c += 1
        i += 1

    while j < n2:
        if c == k:
            ans = arr2[j]
        c += 1
        j += 1

    return ans


# Optimal
# T.C. -> O(log(m+n))
# S.C. -> O(1)


def getnumofElements(k):
    return k


def getKth(a, b, k):
    n1, n2 = len(a), len(b)

    st, en = max(k - n2, 0), min(k, len(a))

    while st <= en:
        totalElements = getnumofElements(k)

        partA = st + (en - st) // 2
        partB = totalElements - partA

        l1 = float("-inf") if partA == 0 else a[partA - 1]
        r1 = float("inf") if partA == n1 else a[partA]

        l2 = float("-inf") if partB == 0 else b[partB - 1]
        r2 = float("inf") if partB == n2 else b[partB]

        if l1 > r2:
            en = partA - 1
        elif l2 > r1:
            st = partA + 1
        elif l1 <= r2 and l2 <= r1:
            return max(l1, l2)
    return 0


def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    n1, n2 = len(arr1), len(arr2)

    # Means nums 2 is smaller
    if n1 > n2:
        return getKth(arr2, arr1, k)

    # Means nums 1 is smaller
    else:
        return getKth(arr1, arr2, k)
