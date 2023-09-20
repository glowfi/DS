# https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n) [Recursion stack space]


def helper(i):
    if i == 0:
        return 0

    return i + helper(i - 1)


def sumFirstN(n: int) -> int:
    return helper(n)


# Optimal
# T.C. -> O(1)
# S.C. -> O(1)


def sumFirstN(n: int) -> int:
    return n * (n + 1) // 2
