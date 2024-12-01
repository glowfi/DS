# NA , Easy

# Brute
# T.C. - O(n^2)
# S.C  - O(n)

import random
from bisect import bisect_right


def insert(arr: list[int], elem: int):
    if len(arr) == 0 or arr[len(arr) - 1] <= elem:  # Edge Case [1,2,3] 4
        arr.append(elem)
        return

    lastElem = arr.pop(-1)
    insert(arr, elem)
    print(arr, elem)
    arr.append(lastElem)


def sort(arr: list[int]):  # [3,2,1] -> [1,2,3]
    if len(arr) == 1:
        return

    lastElem = arr.pop(-1)
    sort(arr)
    insert(arr, lastElem)


# Using binary Search
# pos = bisect_right(arr, lastElem)  # Upper bound point just greater than equals to x
# arr.insert(pos, lastElem)


ls = [random.randint(-100, 100) for _ in range(10)]
print("Unsorted:", ls)
sort(ls)
print("Sorted:", ls)
