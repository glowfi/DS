# https://www.codingninjas.com/codestudio/problems/implement-upper-bound_8165383,Easy


# Smallest index such that arr[idx]>X


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


def upperBound(arr: [int], x: int, n: int) -> int:
    ans = n
    for i in range(len(arr)):
        if arr[i] > x:
            ans = i
            break
    return ans


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


def upperBound(arr: [int], x: int, n: int) -> int:
    ans = n
    st, en = 0, len(arr) - 1

    while st <= en:
        mid = (st + en) // 2

        if arr[mid] <= x:
            st = mid + 1

        elif arr[mid] > x:
            ans = mid
            en = mid - 1
    return ans
