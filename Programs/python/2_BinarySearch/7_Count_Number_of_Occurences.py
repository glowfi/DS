# https://www.codingninjas.com/codestudio/problems/occurrence-of-x-in-a-sorted-array_630456 , Medium


# Brute
# T.C. -> O(n)
# S.C. -> O(1)


def count(arr: [int], n: int, x: int) -> int:
    count = 0

    for i in range(len(arr)):
        if arr[i] == x:
            count += 1

    return count


# Optimal
# T.C. -> O(log(n))
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


def count(arr: [int], n: int, x: int) -> int:
    first = search(arr, x, "first")

    if first == -1:
        return 0

    else:
        last = search(arr, x, "last")
        return last - first + 1
