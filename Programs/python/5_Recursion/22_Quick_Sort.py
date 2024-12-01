# https://www.codingninjas.com/studio/problems/quick-sort_5844 , Medium

# Algorithm
# + Take any element as pivot and place it in its correct place
# + Left will have all elements smaller than pivot and right will have element greater than pivot
# + Place i and j in Left and right
# + First find element greater than pivot for i pointer and stop
# + Second find element smaller than pivot for j pointer and stop
# + Swap element at i,j
# + Repeat above two steps until i crosses j

# Optimal
# T.C. - O(nlog(n)) [Average+Best] O(n^2) [Worst] [stable]
# S.C  - O(1)

from typing import List


def getPivot(arr, st, en):
    i, j = st, en
    pivot = arr[st]

    while i < j:
        # Find element greater than pivot
        while arr[i] <= pivot and i <= en - 1:
            i += 1

        while arr[j] > pivot and j >= st + 1:
            j -= 1

        # Swap if i did not cross j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot
    arr[st], arr[j] = arr[j], arr[st]

    return j


def quickSort(arr: List[int], startIndex: int, endIndex: int):
    # Base case: subarray has only one element
    if startIndex >= endIndex:
        return

    pivot = getPivot(arr, startIndex, endIndex)
    quickSort(arr, startIndex, pivot - 1)
    quickSort(arr, pivot + 1, endIndex)


ls = [5, 4, 3, 2, 1]
ls = [4, 3, 8, 4, 6, 5]
quickSort(ls, 0, len(ls) - 1)
print(ls)
