# NA , Easy


# Better
# T.C. - O(n)
# S.C  - O(n)


def checkArraySorted(idx, ls):
    if idx == len(ls) - 1:
        return True

    if ls[idx] > ls[idx + 1]:
        return False

    return checkArraySorted(idx + 1, ls)


ls = [1, 4, 100, 8, 10]
print(checkArraySorted(0, ls))

ls = [1, 4, 8, 10]
print(checkArraySorted(0, ls))


# Optimal
# T.C. - O(n)
# S.C  - O(n)


def checkArraySorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            return False
    return True
