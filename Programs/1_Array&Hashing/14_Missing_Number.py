# https://www.codingninjas.com/codestudio/problems/missing-number_6680467,Easy

# Brute
# T.C. -> O(n)+O(n)+O(n)
# S.C. -> O(n)


def missingNumber(a: List[int], N: int) -> int:
    for i in range(1, N + 1):
        found = 0
        for j in range(len(a)):
            if i == a[j]:
                found = 1
                break
        if found == 0:
            return i


# Better
# T.C. -> O(n)+O(n)+O(n)
# S.C. -> O(n)


def missingNumber(a: List[int], N: int) -> int:
    h = {}

    for i in range(1, N + 1):
        h[i] = 0

    for i in a:
        h[i] = 1

    for i in h:
        if h[i] == 0:
            return i


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def missingNumber(a: List[int], N: int) -> int:
    current = sum(a)
    required = ((N + 1) * N) // 2

    return abs(required - current)
