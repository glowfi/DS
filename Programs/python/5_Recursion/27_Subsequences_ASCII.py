# NA , Easy

# Brute [Ans in argument]
# T.C. - O(2**n)
# S.C  - O(2**n)


def subSequenceAscii_I(idx: int, proc: str, s: str, res: list[str]):
    if idx == len(s):
        res.append(proc)
        return

    # Take single character
    subSequenceAscii_I(idx + 1, proc + s[idx], s, res)

    # Take ASCII value of single character
    subSequenceAscii_I(idx + 1, proc + str(ord(s[idx])), s, res)

    # Do not take
    subSequenceAscii_I(idx + 1, proc, s, res)


s = "hello"
res = []
subSequenceAscii_I(0, "", s, res)
print(res)


# Brute [Ans in body]
# T.C. - O(2**n)
# S.C  - O(2**n)


def subSequenceAscii_II(idx: int, proc: str, s: str) -> list[str]:
    if idx == len(s):
        return [proc]

    # Take single character
    take = subSequenceAscii_II(idx + 1, proc + s[idx], s)

    # Take ASCII value of single character
    ascii = subSequenceAscii_II(idx + 1, proc + str(ord(s[idx])), s)

    # Do not take
    nottake = subSequenceAscii_II(idx + 1, proc, s)

    return [*take, *ascii, *nottake]


s = "hello"
print(subSequenceAscii_II(0, "", s))
