# NA,Medium

# Optimal
# T.C. -> O(n)+O(min(pos,neg))+O(leftover)=O(n)+o(n)
# S.C. -> O(n/2)+O(n/2) = O(n)


from typing import *


def alternateNumbers(a: List[int]) -> List[int]:
    pos = []
    neg = []

    for i in range(len(a)):
        if a[i] < 0:
            neg.append(a[i])
        else:
            pos.append(a[i])

    if len(pos) > len(neg):
        for i in range(len(neg)):
            a[2 * i] = pos[i]
            a[(2 * i) + 1] = neg[i]

        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            a[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            a[2 * i] = pos[i]
            a[(2 * i) + 1] = neg[i]

        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            a[index] = neg[i]
            index += 1


ls = [-2, -3, 4, 5, 6, 7, 8]

# -2 -3
# 4  5  6  7  8
print(alternateNumbers(ls))
print(ls)
