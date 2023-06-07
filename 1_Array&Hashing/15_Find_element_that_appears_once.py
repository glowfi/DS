# https://www.codingninjas.com/codestudio/problems/find-the-single-element_6680465,Easy

# Brute
# T.C. -> O(n^2)
# S.C. -> O(1)


def getSingleElement(arr: List[int]) -> int:
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                cnt += 1
            if cnt >= 2:
                break
        if cnt == 1:
            return arr[i]


# Better
# T.C. -> O(n)
# S.C. -> O(n)


def getSingleElement(arr: List[int]) -> int:
    h = {}

    for i in arr:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1

    for i in h:
        if h[i] == 1:
            return i


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def getSingleElement(arr: List[int]) -> int:
    xor = 0

    for i in range(len(arr)):
        xor ^= arr[i]

    return xor
