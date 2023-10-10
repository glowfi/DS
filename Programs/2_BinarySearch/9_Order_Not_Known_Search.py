# NA,Easy

# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


# Given a sorted array it is not told whether the array is sorted in ascending or descending,Search for an element x in that array


def bsAsc(arr, X):
    st, en = 0, len(arr) - 1

    while st <= en:
        mid = st + ((en - st) // 2)

        if arr[mid] == X:
            return mid

        elif arr[mid] > X:
            en = mid - 1

        else:
            st = mid + 1
    return -1


def bsDesc(arr, X):
    st, en = 0, len(arr) - 1

    while st <= en:
        mid = st + ((en - st) // 2)

        if arr[mid] == X:
            return mid

        elif arr[mid] > X:
            st = mid + 1

        else:
            en = mid - 1
    return -1


def ordernotKnown(arr, X):
    if arr[0] <= arr[-1]:
        return bsAsc(arr, X)
    else:
        return bsDesc(arr, X)
