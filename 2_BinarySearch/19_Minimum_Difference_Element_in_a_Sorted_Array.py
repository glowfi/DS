# NA, Easy


# Better
# T.C. -> O(log(n))+O(log(n))
# S.C. -> O(1)

# ls=[1,2,4,6,10,34]
# key=7


def ceil(arr, x):
    st, en = 0, len(arr) - 1
    ans = -1

    while st <= en:
        mid = (st + en) // 2

        if arr[mid] >= x:
            ans = mid
            en = mid - 1
        else:
            st = mid + 1
    return arr[ans]


def floor(arr, x):
    st, en = 0, len(arr) - 1
    ans = -1

    while st <= en:
        mid = (st + en) // 2

        if arr[mid] <= x:
            ans = mid
            st = mid + 1
        else:
            en = mid - 1
    return arr[ans]


def min_diff_sorted_array(arr, x):
    _ceil = ceil(arr, x)
    _floor = floor(arr, x)
    return min(_ceil, _floor)


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


def bs(arr, x):
    st, en = 0, len(arr) - 1

    while st <= en:
        mid = (st + en) // 2
        if arr[mid] == x:
            return 0
        elif arr[mid] > x:
            en = mid - 1
        else:
            st = mid + 1
    y1 = abs(x - arr[st])
    y2 = abs(x - arr[en])
    return min(y1, y2)


def min_diff_sorted_array(arr, x):
    return bs(arr, x)


ls = [1, 2, 4, 6, 10, 34]
key = 7

print(min_diff_sorted_array(ls, key))
