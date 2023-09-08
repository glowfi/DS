# https://www.codingninjas.com/studio/problems/row-of-a-matrix-with-maximum-ones_982768, Medium


# Brute
# T.C. -> O(n*m)
# S.C. -> O(1)


def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:
    ridx = -1
    count = 0

    for i in range(len(matrix)):
        c = 0
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                c += 1

        if c > count:
            ridx = i
            count = c

    return ridx


# Optimal
# T.C. -> O(n*log(m))
# S.C. -> O(1)


def search(arr, X, _type):
    st, en = 0, len(arr) - 1
    ans = -1

    while st <= en:
        mid = st + (en - st) // 2

        if arr[mid] == X:
            ans = mid
            if _type == "first":
                en = mid - 1
            else:
                st = mid + 1

        elif arr[mid] < X:
            st = mid + 1

        else:
            en = mid - 1

    return ans


def getCount(arr: [int], x: int) -> int:
    first = search(arr, x, "first")

    if first == -1:
        return 0

    else:
        last = search(arr, x, "last")
        return last - first + 1


def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:
    ridx = -1
    count = 0
    for i in range(len(matrix)):
        countOnes = getCount(matrix[i], 1)
        if countOnes > count:
            ridx = i
            count = countOnes
    return ridx
