# NA , Easy

# Brute [Ans in argument]
# T.C. - O(n!)
# S.C  - O(n)


def countPermutation(arr, idx, processed, count):
    if idx == len(arr):
        count += 1
        return

    for i in range(len(processed) + 1):
        new = processed[:i] + arr[idx] + processed[i:]
        countPermutation(arr, idx + 1, new, count)


# Brute [Ans in body]
# T.C. - O(n!)
# S.C  - O(n)


def countPermutation(arr, idx, processed):
    if idx == len(arr):
        return 1

    tmp = 0

    for place in range(len(processed) + 1):
        new = processed[:place] + arr[idx] + processed[place:]
        val = countPermutation(arr, idx + 1, new)
        tmp += val

    return tmp


ls = ["1", "2", "3"]
val = countPermutation(ls, 0, "")
print(val)
