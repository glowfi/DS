# https://www.codingninjas.com/codestudio/problems/count-subarrays-with-given-xor_1115652,Medium

# Brute
# T.C. -> O(n^2)
# S.C. -> O(n)


def subarraysXor(arr, x):
    c = 0

    for i in range(len(arr)):
        xor = 0
        for j in range(i, len(arr)):
            xor ^= arr[j]
            if xor == x:
                c += 1

    return c


# Optimal
# T.C. -> O(n)
# S.C. -> O(n)


def subarraysXor(arr, x):
    xr = 0
    count = {0: 1}
    c = 0

    for i in range(len(arr)):
        xr ^= arr[i]
        rem = xr ^ x

        if rem in count:
            c += count[rem]

        if xr not in count:
            count[xr] = 1
        else:
            count[xr] += 1

    return c
