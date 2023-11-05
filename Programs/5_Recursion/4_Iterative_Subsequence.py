# NA , NA

# Brute
# T.C. - O(N*2**N)
# S.C  - O(N*2**N)


def iterativeSubsequence(arr):
    outer = [[], [arr[0]]]

    for num in arr[1:]:
        for i in range(len(outer)):
            outer.append([*outer[i], num])

    print(outer)


# Brute
# T.C. - O(N*2**N)
# S.C  - O(N*2**N)


def iterativeSubsequenceDuplicates(arr):
    outer = [[], [arr[0]]]
    arr.sort()

    for ind, num in enumerate(arr[1:]):
        if arr[ind] != arr[ind - 1]:
            for i in range(len(outer)):
                outer.append([*outer[i], num])

    print(outer)


ls = [1, 2, 2, 2]
iterativeSubsequence(ls)
iterativeSubsequenceDuplicates(ls)
