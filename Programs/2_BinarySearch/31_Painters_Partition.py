# https://www.codingninjas.com/studio/problems/painter-s-partition-problem_1089557 , Medium

# Brute
# T.C. -> O((sum(arr)-max(arr))*n)
# S.C. -> O(1)


def getPainters(arr, k, maxArea):
    painter = 1
    boardArea = 0

    for i in range(len(arr)):
        if boardArea + arr[i] <= maxArea:
            boardArea += arr[i]
        else:
            painter += 1
            boardArea = arr[i]

    return painter


def findLargestMinDistance(boards: list, k: int):
    if k > len(boards):
        return -1
    st, en = max(boards), sum(boards) + 1
    for minArea in range(st, en):
        if getPainters(boards, k, minArea) == k:
            return minArea
    return st


# Optimal
# T.C. -> O(log(sum(arr)-max(arr))*n)
# S.C. -> O(1)


def getPainters(arr, k, maxArea):
    painter = 1
    boardArea = 0

    for i in range(len(arr)):
        if boardArea + arr[i] <= maxArea:
            boardArea += arr[i]
        else:
            painter += 1
            boardArea = arr[i]

    return painter


def findLargestMinDistance(boards: list, k: int):
    if k > len(boards):
        return -1

    st, en = max(boards), sum(boards)

    while st <= en:
        mid = st + (en - st) // 2

        if getPainters(boards, k, mid) > k:
            st = mid + 1
        else:
            en = mid - 1

    return st
