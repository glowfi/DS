# NA , Easy

# Recursive Tree
# https://0x0.st/HtUm.763.png

# Brute [Ans in argument]
# T.C. - O(n!)
# S.C  - O(n)


def generatePermutation_I(idx: int, proc: str, res: list[str], s: str):
    if idx == len(s):
        res.append(proc)
        return

    tmp = []

    for i in range(len(proc) + 1):
        newString = proc[:i] + s[idx] + proc[i:]
        val = generatePermutation_I(idx + 1, newString, res, s)


s = "abc"
res = []
generatePermutation_I(0, "", res, s)
print(res)


# Brute [Ans in body]
# T.C. - O(n!)
# S.C  - O(n)


def generatePermutation_II(idx: int, proc: str, s: str) -> list[str]:
    if idx == len(s):
        return [proc]

    tmp = []
    for i in range(len(proc) + 1):
        newString = proc[:i] + s[idx] + proc[i:]
        val = generatePermutation_II(idx + 1, newString, s)
        for i in val:
            tmp.append(i)

    return tmp


s = "abc"
print(generatePermutation_II(0, "", s))
