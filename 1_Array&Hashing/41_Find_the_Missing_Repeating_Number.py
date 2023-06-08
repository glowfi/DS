# https://www.codingninjas.com/codestudio/problems/missing-and-repeating-numbers_6828164 , Medium

# Brute
# T.C. -> O(N)*O(n)
# S.C. -> O(m+n)


def findMissingRepeatingNumbers(a: [int]) -> [int]:
    N = len(a)
    miss, rep = -1, -1

    for i in range(1, N + 1):
        cnt = 0
        for j in range(len(a)):
            if a[j] == i:
                cnt += 1
        if cnt == 0:
            miss = i
        if cnt > 1:
            rep = i

    return [rep, miss]


# Better
# T.C. -> O(n)+O(n)+O(n)
# S.C. -> O(n)


def findMissingRepeatingNumbers(a: [int]) -> [int]:
    N = len(a)
    rep, miss = -1, -1

    h = {i: 0 for i in range(1, N + 1)}

    for i in range(len(a)):
        if a[i] in h:
            h[a[i]] += 1

    for i in h:
        if h[i] > 1:
            rep = i
        elif h[i] == 0:
            miss = i

    return [rep, miss]


# Optimal
# T.C. -> O(n)+O(n)
# S.C. -> O(1)


def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a)

    # Find Sum of the given array
    s = 0
    for i in range(len(a)):
        s += a[i]

    # Find sum of 1 to N
    s1 = (n * (n + 1)) // 2

    K1 = s - s1

    # Find Sum of squares the given array
    s = 0
    for i in range(len(a)):
        s += a[i] * a[i]

    # Find sum of squares of 1 to N
    s2 = (n * (n + 1) * (2 * n + 1)) // 6

    K2 = s - s2

    # y-x =K1

    # y+x
    K3 = K2 // K1

    rep = (K1 + K3) // 2
    miss = rep - K1

    return [rep, miss]
