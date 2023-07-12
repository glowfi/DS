# NA, Easy


# Optimal
# T.C. -> O(infinity)+log(k)
# S.C. -> O(infinity)

# ls=[0,0,0,0,.......,1,1,1,.....]
# key=Postion of 1st 1


def BS(st, en, arr, X):
    while st <= en:
        mid = st + ((en - st) // 2)

        if arr[mid] == X:
            en = mid - 1
        else:
            st = mid + 1
    return st


def getPos(arr):
    st, en = 0, 1
    X = 1

    while True:
        mid = st + ((en - st) // 2)

        if arr[mid] == 1:
            break

        elif arr[mid] < X:
            st = en
            en *= 2

    return BS(st, en, arr, X)
