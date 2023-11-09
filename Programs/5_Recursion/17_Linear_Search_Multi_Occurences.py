# NA , Easy

# Brute [Ans in body]
# T.C. - O(n)
# S.C  - O(n)


def linSearchMulti(idx, arr, target) -> list[int]:
    if idx == len(arr):
        return []

    res = []

    if idx == len(arr):
        res.append(idx)

    val = linSearchMulti(idx + 1, arr, target)

    return [*res, *val]
