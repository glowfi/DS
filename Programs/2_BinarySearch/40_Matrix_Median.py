# https://www.codingninjas.com/studio/problems/median-of-a-row-wise-sorted-matrix_1115473 , Medium


# Brute
# T.C. -> O(n*m)+O((n*m)log(n*m))
# S.C. -> O(n*m)


def median(matrix: [[int]], m: int, n: int) -> int:
    ls = []

    for i in range(m):
        for j in range(n):
            ls.append(matrix[i][j])

    ls.sort()
    mid = (m * n) // 2
    return ls[mid]


# Optimal
# T.C. -> O(ro)+O(ro*log(co))
# S.C. -> O(1)


def gethowManySmaller(arr, target):
    st, en = 0, len(arr) - 1
    ans = len(arr)

    while st <= en:
        mid = st + (en - st) // 2

        if arr[mid] > target:
            ans = mid
            en = mid - 1
        else:
            st = mid + 1

    return ans


def median(matrix: [[int]], m: int, n: int) -> int:
    countRequired = (m * n + 1) // 2

    st, en = -1, -1

    for i in range(m):
        st = min(st, matrix[i][0])
        en = max(st, matrix[i][n - 1])

    while st <= en:
        mid = st + (en - st) // 2

        c = 0
        for i in range(m):
            c += gethowManySmaller(matrix[i], mid)

        if c < countRequired:
            st = mid + 1
        else:
            en = mid - 1

    return st
