# https://www.codingninjas.com/codestudio/problems/ceiling-in-a-sorted-array_1825401,Medium


# Floor -> Largest number in the array such that number<=x
# Ceil  -> Smallest number in the array such that number>=x


# Optimal
# T.C. -> O(log(n))+O(log(n))
# S.C. -> O(1)


def floor(arr, x):
    st, en = 0, len(arr) - 1
    ans = -1

    while st <= en:
        mid = st + (en - st) // 2

        if arr[mid] <= x:
            ans = arr[mid]
            st = mid + 1
        else:
            en = mid - 1
    return ans


def ceil(arr, x):
    st, en = 0, len(arr) - 1
    ans = -1

    while st <= en:
        mid = st + (en - st) // 2

        if arr[mid] >= x:
            ans = arr[mid]
            en = mid - 1
        else:
            st = mid + 1
    return ans


def ceilingInSortedArray(n, x, arr):
    arr.sort()
    fl = floor(arr, x)
    cl = ceil(arr, x)
    ans = [fl, cl]

    print(fl, end=" ")
    return cl
