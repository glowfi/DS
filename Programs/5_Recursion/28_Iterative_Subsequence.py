# NA , Easy

# Generate Subsequences iteratively

# Brute
# T.C. - O(N*2**N)
# S.C  - O(N*2**N)


def iterativeSubsequence(arr):
    outer = [[arr[0]], []]
    for i in range(1, len(arr)):
        currNum = arr[i]
        for j in range(0, len(outer)):
            tmp = [*outer[j], currNum]
            outer.append(tmp)
    print(outer, len(outer))


ls = [1, 2, 3]
iterativeSubsequence(ls)


# Generate Subsequences iteratively remove duplicate subsequences

# Brute
# T.C. - O(N*2**N)
# S.C  - O(N*2**N)


def iterativeSubsequenceDuplicates(arr: list[int]):
    outer = [[arr[0]], []]
    arr.sort()
    for i in range(1, len(arr)):
        currNum = arr[i]
        if arr[i] != arr[i - 1]:
            for j in range(0, len(outer)):
                tmp = [*outer[j], currNum]
                outer.append(tmp)
    print(outer, len(outer))


ls = [1, 2, 3]
iterativeSubsequenceDuplicates(ls)
