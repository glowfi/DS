# NA,Easy

# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


# Given a sorted array it is not told whether the array is sorted in ascending or descending,Search for an element x in that array


def bsAsc(arr, x):
    st, en = 0, len(arr) - 1

    while st <= en:
        mid = (st + en) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            en = mid - 1

        else:
            st = mid + 1

    return -1


def bsDesc(arr, x):
    st, en = 0, len(arr) - 1

    while st <= en:
        mid = (st + en) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            st = mid + 1

        else:
            en = mid - 1

    return -1


def orderNotKnown(arr, x):
    # if ascending (If first element is smaller that last)
    if arr[0] < arr[-1]:
        return bsAsc(arr, x)

    # if descending (If first element is greater than last)
    if arr[0] > arr[-1]:
        return bsAsc(arr, x)
    return bsDesc(arr, x)
