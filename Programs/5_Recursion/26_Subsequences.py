# NA , Easy

# Brute [Ans in argument]
# T.C. - O(2**n)
# S.C  - O(2**n)

# Recursive Tree
# https://0x0.st/HtlE.362.png


def generateSubsequences_I(idx: int, proc: str, res: list[str], s: str):
    # Append the processed string in final result
    if idx == len(s):
        res.append(proc)
        return

    # Take current character
    generateSubsequences_I(idx + 1, proc + s[idx], res, s)

    # Do not take current character
    generateSubsequences_I(idx + 1, proc, res, s)


s = "helo"
res = []
generateSubsequences_I(0, "", res, s)
print(res)


# Brute [Ans in body]
# T.C. - O(2**n)
# S.C  - O(2**n)


def generateSubsequences_II(idx: int, tmp: str, s: str) -> list[str]:
    if idx == len(s):
        return [tmp]

    take = generateSubsequences_II(idx + 1, tmp + s[idx], s)
    nottake = generateSubsequences_II(idx + 1, tmp, s)

    return [*take, *nottake]


s = "helo"
print(generateSubsequences_II(0, "", s))
