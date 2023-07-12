# NA, Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(1)


def min_diff_sorted_array(arr, x):
    mn = float("inf")
    for i in range(len(arr)):
        if abs(arr[i] - x):
            mn = min(arr[i] - x, mn)
    return mn


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)

# ls=[1,2,4,6,10,34]
# key=9


def min_diff_sorted_array(arr, x):
    st, en = 0, len(arr) - 1

    while st <= en:
        mid = st + ((en - st) // 2)

        if arr[mid] == x:
            return arr[mid]

        elif arr[mid] > x:
            en = mid - 1

        else:
            st = mid + 1

    y1 = abs(arr[st] - x)
    y2 = abs(arr[en] - x)

    return min(y1, y2)


ls = [1, 2, 4, 6, 10, 34]
key = 9

print(min_diff_sorted_array(ls, key))
