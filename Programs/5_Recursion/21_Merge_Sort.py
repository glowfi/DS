# NA , Medium

# Algorithm
# + Keep Dividing the array into 2 halves until we reach array with only one element
# + Then apply merge sorted array on 2 sorted arrays as a single array is already sorted

# Optimal
# T.C. - O(nlog(n)) [Worst+Average+Best] [stable]
# S.C  - O(1)


# Recursive Tree
# https://0x0.st/HtwV.291.png


def mergeSort(arr, low, hi):
    if low >= hi:
        return

    mid = (low + hi) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, hi)
    sort2sortedlist(arr, low, mid, hi)


def sort2sortedlist(arr, lo, mid, hi):
    i, j = lo, mid + 1
    m, n = mid, hi
    tmp = []

    while i <= m and j <= n:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= m:
        tmp.append(arr[i])
        i += 1
    while j <= n:
        tmp.append(arr[j])
        j += 1

    idx = 0
    for k in range(lo, hi + 1):
        arr[k] = tmp[idx]
        idx += 1


ls = [5, 4, 3, 100, 2, 1, -1, -2, 0]
mergeSort(ls, 0, len(ls) - 1)
print(ls)
