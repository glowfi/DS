# NA , Easy

# Imagine st = "bcdappledef" output="bcddef" [Skip apple]

# Brute (Ans in argument)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]


def skipString(idx: int, st: str, out: str):
    if idx == len(st):
        return out

    if st[idx:].startswith("apple"):
        return skipString(idx + len("apple"), st, out)

    return skipString(idx + 1, st, out + st[idx])


# Imagine st = "bcdappledef" output="bcdappledef" [Do not skip when it is apple]
# Imagine st = "bcdappxydef" output="bcdxydef" [Skip app when it is not apple]

# Brute (Ans in argument)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]


def skipString(idx: int, st: str, out: str):
    if idx == len(st):
        return out

    if st[idx:].startswith("app") and not st[idx:].startswith("apple"):
        return skipString(idx + len("app"), st, out)
    return skipString(idx + 1, st, out + st[idx])
