# https://www.codingninjas.com/codestudio/problems/lower-bound_8165382,Easy


# Smallest index such that arr[idx]>=X


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(len(arr)):
        if arr[i] >= x:
            return i
    return n


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


def lowerBound(arr: [int], n: int, x: int) -> int:
    st, en = 0, len(arr) - 1
    ans = n

    while st <= en:
        mid = st + ((en - st) // 2)
        if arr[mid] >= x:
            ans = mid
            en = mid - 1
        else:
            st = mid + 1
    return ans
