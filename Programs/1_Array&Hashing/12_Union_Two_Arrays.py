# https://www.codingninjas.com/codestudio/problems/sorted-array_6613259,Easy

from typing import *

# Brute
# T.C. -> O(n)+O(n)+O(nlog(n))
# S.C. -> O(n)


def sortedArray(a: [int], b: [int]) -> [int]:
    return sorted(list(set([*a, *b])))


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def sortedArray(a: [int], b: [int]) -> [int]:
    ans = []

    i, j = 0, 0
    m, n = len(a), len(b)

    while i < m and j < n:
        if a[i] <= b[j]:
            if len(ans) == 0 or ans[-1] != a[i]:
                ans.append(a[i])
            i += 1
        else:
            if len(ans) == 0 or ans[-1] != b[j]:
                ans.append(b[j])
            j += 1
        # print(ans)

    while i < m:
        if ans[-1] != a[i]:
            ans.append(a[i])
        i += 1
    while j < n:
        if ans[-1] != b[j]:
            ans.append(b[j])
        j += 1

    return ans


a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 4, 5]

print(sortedArray(a, b))
