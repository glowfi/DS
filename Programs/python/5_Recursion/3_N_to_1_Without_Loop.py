# https://www.codingninjas.com/studio/problems/print-1-to-n_628290 , Easy

# Optimal [ans in argument]
# T.C. - O(n)
# S.C  - O(n)

from typing import List


def helper(idx, res):
    if idx == 0:
        return

    res.append(idx)
    helper(idx - 1, res)


def printNos(x: int) -> List[int]:
    res = []
    helper(x, res)
    return res


# Optimal [ans in body]
# T.C. - O(n)
# S.C  - O(n)


def printNos(x: int) -> List[int]:
    if x == 0:
        return []

    val = printNos(x - 1)

    return [x, *val]
