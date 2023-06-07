# https://www.codingninjas.com/codestudio/problems/intersection-of-2-arrays_1082149,Easy

# Brute
# T.C. -> O(n1*n2)
# S.C. -> O(n2)


def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    ans = []
    vis = [0] * len(brr)
    for i in range(len(arr)):
        for j in range(len(brr)):
            if vis[j] == 0 and arr[i] == brr[j]:
                vis[j] = 1
                ans.append(arr[i])
                break
            if brr[j] > arr[i]:
                break

    return ans


# Optimal
# T.C. -> O(n1+n2)
# S.C. -> O(1)


def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    ans = []
    i, j = 0, 0
    n1 = len(arr)
    n2 = len(brr)

    while i < n1 and j < n2:
        if arr[i] < brr[j]:
            i += 1

        elif brr[j] < arr[i]:
            j += 1

        else:
            ans.append(arr[i])
            i += 1
            j += 1

    return ans
