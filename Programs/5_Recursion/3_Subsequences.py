# NA , NA

# Brute [Ans in argument]
# T.C. - O(2**n)
# S.C  - O(2**n)


def subSequence(idx: int, processed: str, s: str, out: list[str]):
    if idx == len(s):
        out.append(processed)
        return out

    # Take current
    # add to processed
    subSequence(idx + 1, processed + s[idx], s, out)

    # Do not take current
    subSequence(idx + 1, processed, s, out)


# Brute [Ans in body]
# T.C. - O(2**n)
# S.C  - O(2**n)


def subSequence(idx: int, processed: str, s: str) -> list[str]:
    if idx == len(s):
        return [processed]

    # Take current
    # add to processed
    take = subSequence(idx + 1, processed + s[idx], s)

    # Do not take current
    notTake = subSequence(idx + 1, processed, s)

    return [*take, *notTake]
