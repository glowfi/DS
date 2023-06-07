# https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/1,Easy

# Brute
# T.C. -> O(n*log(n))
# S.C. -> O(n)


def largest(arr, n):
    arr.sort()
    return arr[-1]


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def largest(arr, n):
    mx = float("-inf")
    for i in range(len(arr)):
        if arr[i] >= mx:
            mx = arr[i]
    return mx
