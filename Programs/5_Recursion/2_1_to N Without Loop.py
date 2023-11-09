# https://www.codingninjas.com/studio/problems/print-1-to-n_628290 , Easy

# Recursive Tree
# https://0x0.st/Htww.774.png


# Optimal [ans in argument]
# T.C. - O(n)
# S.C  - O(n)

from typing import List


def helper(idx, res, n):
    if idx == n + 1:
        return
    res.append(idx)
    helper(idx + 1, res, n)


def printNos(x: int) -> List[int]:
    res = []
    helper(1, res, x)
    return res


# Optimal [ans in body]
# T.C. - O(n)
# S.C  - O(n)

from typing import List


def printNos(x: int) -> List[int]:
    if x == 0:
        return []
    res = []
    val = printNos(x - 1)
    return [*val, x]
