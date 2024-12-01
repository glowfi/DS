# https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068 , Easy


# Better
# T.C. - O(n) [ans in body]
# S.C  - O(n)

from typing import List


def sumFirstN(n: int) -> int:
    if n == 0:
        return 0

    return n + sumFirstN(n - 1)


# Better
# T.C. - O(1)
# S.C  - O(1)

from typing import List


def sumFirstN(n: int) -> int:
    return n * (n + 1) // 2
