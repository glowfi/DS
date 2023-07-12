# NA, Easy


# Optimal
# T.C. -> O(log(n))
# S.C. -> O(1)


# Smallest among all the numbers greater than x
def ceil(x, arr):
    st, en = 0, len(arr) - 1
    ans = -1

    while st <= en:
        mid = st + ((en - st) // 2)

        if ord(arr[mid]) > ord(x):
            ans = mid
            en = mid - 1
        else:
            st = mid + 1

    return ans


# Given alphabets array
alphabets = ["a", "c", "f", "h", "l", "q"]
x = "l"

print(ceil(x, alphabets))
