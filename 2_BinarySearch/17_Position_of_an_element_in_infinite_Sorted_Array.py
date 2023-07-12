# NA, Easy


# Optimal
# T.C. -> O(infinity)+log(k)
# S.C. -> O(infinity)

# ls=[1,2,3,4,5,6,7,........]
# key=90


def BS(st, en, arr, X):
    while st <= en:
        mid = st + ((en - st) // 2)

        if arr[mid] == X:
            return mid

        elif arr[mid] < X:
            st = mid + 1

        else:
            en = mid - 1
    return -1


def getPos(arr, X):
    st, en = 0, 1
    ans = -1

    while True:
        mid = st + ((en - st) // 2)

        if arr[mid] < X:
            st = en
            en *= 2

        elif arr[mid] >= X:
            ans = mid
            break

    # By chance if we stop at our target number X
    if arr[ans] == X:
        return mid

    return BS(st, en, arr, X)
