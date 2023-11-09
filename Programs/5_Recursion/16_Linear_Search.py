# NA , Easy

# Brute
# T.C. - O(n)
# S.C  - O(n)


def linearSearch(idx, arr, target):
    if idx == len(arr):
        return -1

    if arr[idx] == target:
        return idx

    linearSearch(idx + 1, arr, target)
