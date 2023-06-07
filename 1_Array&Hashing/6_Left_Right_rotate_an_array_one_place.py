# NoLINK,Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


# left(1) ->[2,3,4,5,1]


def left(ls):
    for i in range(len(ls) - 1):
        ls[i], ls[i + 1] = ls[i + 1], ls[i]
    return ls


print(left([1, 2, 3, 4, 5]))


# right(1) ->[5,1,2,3,4]


def right(ls):
    for i in range(len(ls) - 1, 0, -1):
        ls[i], ls[i - 1] = ls[i - 1], ls[i]
    return ls


print(right([1, 2, 3, 4, 5]))
