# https://practice.geeksforgeeks.org/problems/reversal-algorithm5340/1,Easy

# Brute
# T.C. -> O(k*n)
# S.C. -> O(1)


def left(ls, k):
    k = k % len(ls)

    for i in range(k):
        for i in range(len(ls) - 1):
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
    return ls


print(left([1, 2, 3, 4, 5], 3))


# Optimal
# T.C. -> O(n)+O(k)+O(n-k)
# S.C. -> O(1)


# Left
class Solution:
    def leftRotate(self, arr, n, d):
        k = d
        k = k % len(arr)

        def rev(i, j, arr):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        rev(0, k - 1, arr)
        rev(k, len(arr) - 1, arr)
        rev(0, len(arr) - 1, arr)
