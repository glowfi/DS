# NA , Medium

# Given ab (change case of the subsequences)
# Ouput -> ab aB Ab AB

# Brute
# T.C. - O(2^n)
# S.C  - O(n)


def solve(idx, tmp, st: str):
    if idx == len(st):
        return [tmp[:]]

    ans = []

    # Take small of current character
    first = solve(idx + 1, tmp + st[idx], st)
    for i in first:
        ans.append(i)

    # Take big of current character
    sec = solve(idx + 1, tmp + st[idx].upper(), st)
    for i in sec:
        ans.append(i)

    return ans


st = "abc"
st = "ab"
print(solve(0, "", st))
