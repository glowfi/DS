# https://www.codingninjas.com/studio/problems/factorial-numbers-not-greater-than-n_8365435 , Easy


# Optimal
# T.C. - O(m)
# S.C  - O(m)

from typing import *


def getFac(n):
    if n <= 0:
        return 1

    return n * getFac(n - 1)


def factorialNumbers(n: int) -> List[int]:
    res = []

    i = 1
    while True:
        k = getFac(i)
        if k > n:
            break
        res.append(k)
        i += 1

    return res
