# NA , Easy


# Imagine string s="basdasa" output="bsds" [Remove all a character]

# Brute (Ans in argument)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]


def getString_I(idx, st, res):
    if idx == len(st):
        return res

    if st[idx] == "a":
        return getString_I(idx + 1, st, res)

    return getString_I(idx + 1, st, res + st[idx])


# Brute (Ans in body)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]


def getString_II(idx, st):
    if idx == len(st):
        return ""

    if st[idx] != "a":
        return st[idx] + getString_II(idx + 1, st)

    return "" + getString_II(idx + 1, st)
