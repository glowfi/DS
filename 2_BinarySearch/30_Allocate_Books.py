# https://www.codingninjas.com/studio/problems/allocate-books_1090540 , Medium

# Brute
# T.C. -> O((sum(arr)-max(arr))*n)
# S.C. -> O(1)


def canAllocate(arr, m, maxPage):
    stud = 1
    pages = 0

    for i in range(len(arr)):
        if pages + arr[i] <= maxPage:
            pages += arr[i]
        else:
            stud += 1
            pages = arr[i]

    return stud == m


def findPages(arr: [int], n: int, m: int) -> int:
    if m > n:
        return -1

    st, en = max(arr), sum(arr)

    for minPages in range(st, en + 1):
        if canAllocate(arr, m, minPages):
            return minPages
    return st


# Optimal
# T.C. -> O(log(sum(arr)-max(arr))*n)
# S.C. -> O(1)


def canAllocate(arr, m, maxPage):
    stud = 1
    pages = 0

    for i in range(len(arr)):
        if pages + arr[i] <= maxPage:
            pages += arr[i]
        else:
            stud += 1
            pages = arr[i]

    return stud


def findPages(arr: [int], n: int, m: int) -> int:
    if m > n:
        return -1

    st, en = max(arr), sum(arr)

    while st <= en:
        mid = st + (en - st) // 2

        if canAllocate(arr, m, mid) > m:
            st = mid + 1
        else:
            en = mid - 1

    return st
