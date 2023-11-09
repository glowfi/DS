# NA , Easy

# Imagine st = "bcdappledef" output="bcddef" [Skip apple]

# Brute (Ans in argument)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]


def skipString_I(idx: int, s: str, res: str, skipString: str) -> str:
    if idx == len(s):
        return res

    # Skip if startswith skipString
    if s[idx:].startswith(skipString):
        return skipString_I(idx + len(skipString), s, res, skipString)

    # Append the current character if does not startswith skipString
    return skipString_I(idx + 1, s, res + s[idx], skipString)


st = "bcdappledef"
skipString = "apple"
print(skipString_I(0, st, "", skipString))

# Brute (Ans in body)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]

# Recursive Tree
# https://0x0.st/Htl9.820.png


def skipString_II(idx: int, s: str, skipString: str) -> str:
    if idx == len(s):
        return ""

    if s[idx:].startswith(skipString):
        return skipString_II(idx + len(skipString), s, skipString)

    return s[idx] + skipString_II(idx + 1, s, skipString)


st = "bcdappledef"
skipString = "apple"
print(skipString_II(0, st, skipString))
