# NA,Easy

# Optimal (Iterative)
# T.C. -> O(log(n))
# S.C. -> O(1)


def bsDesc(nums, X):
    st, en = 0, len(nums) - 1

    while st <= en:
        mid = st + ((en - st) // 2)

        if nums[mid] == X:
            return mid

        elif nums[mid] > X:
            st = mid + 1

        else:
            en = mid - 1

    return -1


# Optimal (Recursive)
# T.C. -> O(log(n))
# S.C. -> O(1)


def _bsDesc(nums, X, st, en):
    if st > en:
        return -1

    mid = st + ((en - st) // 2)

    if nums[mid] == X:
        return mid

    elif nums[mid] > X:
        return _bsDesc(nums, X, mid + 1, en)

    else:
        return _bsDesc(nums, X, st, mid - 1)


# List
ls = [9, 8, 7, 6, 5]

# Iterative
pos1 = bsDesc(ls, 8)
pos2 = bsDesc(ls, 0)
print(pos1)
print(pos2)

# Recursive
pos1 = _bsDesc(ls, 9, 0, len(ls) - 1)
pos2 = _bsDesc(ls, 0, 0, len(ls) - 1)
print(pos1)
print(pos2)
