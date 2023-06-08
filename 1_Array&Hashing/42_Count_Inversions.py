# https://www.codingninjas.com/codestudio/problems/number-of-inversions_6840276 , Medium

# i<j and arr[i]>arr[j]

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


def numberOfInversions(a: List[int], n: int) -> int:
    c = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                c += 1
    return c


# Optimal
# T.C. -> O(nlog(n))
# S.C. -> O(n)


def merge(arr, l, m, r, c):
    i, j = l, m + 1
    s1 = m
    s2 = r
    tmp = []

    while i <= s1 and j <= s2:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        elif arr[j] <= arr[i]:
            c[0] += m + 1 - i
            tmp.append(arr[j])
            j += 1

    while i <= s1:
        tmp.append(arr[i])
        i += 1

    while j <= s2:
        tmp.append(arr[j])
        j += 1

    k = 0
    for i in range(l, r + 1):
        arr[i] = tmp[k]
        k += 1


def mergeSort(arr, l, r, c):
    if l >= r:
        return

    mid = (l + r) // 2

    mergeSort(arr, l, mid, c)
    mergeSort(arr, mid + 1, r, c)
    merge(arr, l, mid, r, c)


def numberOfInversions(a: List[int], n: int) -> int:
    c = [0]
    mergeSort(a, 0, len(a) - 1, c)
    return c[0]
