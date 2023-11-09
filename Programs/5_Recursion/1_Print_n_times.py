# https://www.codingninjas.com/studio/problems/-print-n-times_8380707 , Easy


# Optimal
# T.C. - O(n)
# S.C  - O(n)


from typing import *


def printNtimes(n: int) -> None:
    if n == 0:
        return

    print("Coding Ninjas", end=" ")
    printNtimes(n - 1)
