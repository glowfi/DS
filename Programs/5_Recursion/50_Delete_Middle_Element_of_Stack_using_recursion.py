# NA , Easy

# Brute
# T.C. - O(k)
# S.C  - O(n)


def _delmid(stk, idx, mid):
    if idx == mid:
        stk.pop(-1)
        return

    lastElem = stk.pop(-1)
    _delmid(stk, idx - 1, mid)
    stk.append(lastElem)


def delmid(stk, mid):
    if len(stk) == mid:
        stk.pop(-1)
        return

    lastElem = stk.pop(-1)
    delmid(stk, mid)
    stk.append(lastElem)


ls = [5, 4, 3, 2, 1]
delmid(ls, (len(ls) // 2) + 1)
print(ls)

ls = [5, 4, 3, 2, 1]
_delmid(ls, len(ls) - 1, (len(ls) // 2))
print(ls)
