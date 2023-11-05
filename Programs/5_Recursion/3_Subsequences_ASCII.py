# NA , NA

# Brute [Ans in argument]
# T.C. - O(2**n)
# S.C  - O(2**n)


def subSequenceAscii(idx: int, processed: str, s: str, out: list[str]):
    if idx == len(s):
        out.append(processed)
        return out

    # Take current
    # add to processed
    subSequenceAscii(idx + 1, processed + s[idx], s, out)

    # take Ascii
    subSequenceAscii(idx + 1, processed + str(ord(s[idx])), s, out)

    # Do not take current
    subSequenceAscii(idx + 1, processed, s, out)


# Brute [Ans in body]
# T.C. - O(2**n)
# S.C  - O(2**n)


def subSequenceAscii(idx: int, processed: str, s: str, out: list[str]) -> list[str]:
    if idx == len(s):
        out.append(processed)
        return out

    # Take current
    # add to processed
    take = subSequenceAscii(idx + 1, processed + s[idx], s, out)

    # take Ascii
    ascii = subSequenceAscii(idx + 1, processed + str(ord(s[idx])), s, out)

    # Do not take current
    notTake = subSequenceAscii(idx + 1, processed, s, out)

    return [*take, *ascii, *notTake]
