# https://www.codingninjas.com/studio/problems/aggressive-cows_1082559 , Medium

# Brute
# T.C. -> O(nlog(n))+O((max(stalls)-min(stalls))*n)
# S.C. -> O(1)


def canbePlaced(arr, dis, k):
    placed = 1
    last = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - last >= dis:
            placed += 1
            last = arr[i]

        if placed == k:
            return True
    return False


def aggressiveCows(stalls, k):
    stalls.sort()
    minDis = -1
    for distance in range(1, stalls[-1] - stalls[0]):
        if not canbePlaced(stalls, distance, k):
            break
        minDis = distance
    return minDis


# Optimal
# T.C. -> O(nlog(n))+O(log(max(stalls)-min(stalls))*n)
# S.C. -> O(1)


def canbePlaced(arr, dis, k):
    placed = 1
    last = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - last >= dis:
            placed += 1
            last = arr[i]

        if placed == k:
            return True
    return False


def aggressiveCows(stalls, k):
    stalls.sort()
    st, en = 1, stalls[-1] - stalls[0]

    while st <= en:
        mid = st + (en - st) // 2

        if canbePlaced(stalls, mid, k):
            st = mid + 1
        else:
            en = mid - 1

    return en
