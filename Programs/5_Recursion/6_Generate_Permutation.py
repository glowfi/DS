# NA , Easy

# Brute [Ans in argument]
# T.C. - O(n!)
# S.C  - O(n)


def generatePermutation(arr, idx, processed, res):
    if idx == len(arr):
        res.append(processed)
        return

    for i in range(len(processed) + 1):
        new = processed[:i] + arr[idx] + processed[i:]
        generatePermutation(arr, idx + 1, new, res)


# Brute [Ans in body]
# T.C. - O(n!)
# S.C  - O(n)


def generatePermutation(arr, idx, processed):
    if idx == len(arr):
        return [processed]

    tmp = []

    for place in range(len(processed) + 1):
        new = processed[:place] + arr[idx] + processed[place:]
        val = generatePermutation(arr, idx + 1, new)
        for i in val:
            tmp.append(i)

    return tmp


ls = ["1", "2", "3"]
res = []
generatePermutation(ls, 0, "", res)
print(res)
