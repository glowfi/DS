# NA , Easy

# Imagine st = "bcdappledef" output="bcdappledef" [Do not skip when it is apple]
# Imagine st = "bcdappxydef" output="bcdxydef" [Skip app when it is not apple]

# Brute (Ans in argument)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]


def skipString_III(
    idx: int, s: str, res: str, skipstring: str, beginswithstring
) -> str:
    if idx == len(s):
        return res

    if not s[idx:].startswith(beginswithstring) and s[idx:].startswith("app"):
        return skipString_III(
            idx + len(skipstring), s, res, skipstring, beginswithstring
        )

    return skipString_III(idx + 1, s, res + s[idx], skipstring, beginswithstring)


st = "bcdappledef"
beginswithstring = "apple"
skipstring = "app"
print(skipString_III(0, st, "", skipstring, beginswithstring))

st = "bcdappxydef"
beginswithstring = "apple"
skipstring = "app"
print(skipString_III(0, st, "", skipstring, beginswithstring))

# Brute (Ans in body)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]


def skipString_IV(idx: int, s: str, skipstring: str, beginswithstring) -> str:
    if idx == len(s):
        return ""

    if not s[idx:].startswith(beginswithstring) and s[idx:].startswith(skipstring):
        return skipString_IV(idx + len(skipstring), s, skipstring, beginswithstring)

    return s[idx] + skipString_IV(idx + 1, s, skipstring, beginswithstring)


st = "bcdappledef"
beginswithstring = "apple"
skipstring = "app"
print(skipString_IV(0, st, skipstring, beginswithstring))

st = "bcdappxydef"
beginswithstring = "apple"
skipstring = "app"
print(skipString_IV(0, st, skipstring, beginswithstring))
