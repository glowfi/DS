# NA , Easy


# Imagine string s="basdasa" output="bsds" [Remove all 'a' character from the string]

# Brute (Ans in argument)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]


def skipCharacter_I(idx, s, res):
    if idx == len(s):
        return res

    if s[idx] != "a":
        res += s[idx]

    return skipCharacter_I(idx + 1, s, res)


print(skipCharacter_I(0, "basdasa", ""))


# Brute (Ans in body)
# T.C. - O(n)
# S.C  - O(n) [Recursion stack space]

# Recursive Tree
# https://0x0.st/Htl2.459.png


def skipCharacter_II(idx, s):
    if idx == len(s):
        return ""

    res = ""

    if s[idx] != "a":
        res += s[idx] + skipCharacter_II(idx + 1, s)
        return res

    return skipCharacter_II(idx + 1, s)


print(skipCharacter_II(0, "basdasa"))
