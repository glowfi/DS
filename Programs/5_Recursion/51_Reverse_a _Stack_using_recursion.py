# NA , Easy

# Brute
# T.C. - O(n^2)
# S.C  - O(n)


def _insert(stk, elem):
    if len(stk) == 0:
        stk.append(elem)
        return

    last = stk.pop(-1)
    _insert(stk, elem)
    stk.append(last)


def revStack(stk: list[int]):  # 5 4 3 2 1 -> 1 2 3 4 5
    if len(stk) == 1:
        return

    lastElem = stk.pop(-1)
    revStack(stk)
    _insert(stk, lastElem)


stk = [1, 2, 34, 5, 6, -1]
print(stk)
revStack(stk)
print(stk)
