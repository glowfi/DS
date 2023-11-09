# NA , Easy

# Brute [Ans in argument]
# T.C. - O(n!)
# S.C  - O(n)


def countPermutation_I(idx, proc, s, resCount) -> None:
    if idx == len(s):
        resCount[0] += 1
        return

    for i in range(len(proc) + 1):
        newString = proc[:i] + s[idx] + proc[i:]
        countPermutation_I(idx + 1, newString, s, resCount)


s = "abc"
res = [0]
countPermutation_I(0, "", s, res)
print(res[0])

# Brute [Ans in body]
# T.C. - O(n!)
# S.C  - O(n)


def countPermutation_II(idx, proc, s) -> int:
    if idx == len(s):
        return 1

    count = 0
    for i in range(len(proc) + 1):
        newString = proc[:i] + s[idx] + proc[i:]
        count += countPermutation_II(idx + 1, newString, s)

    return count


s = "abc"
print(countPermutation_II(0, "", s))
