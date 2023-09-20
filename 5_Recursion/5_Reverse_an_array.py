# https://www.codingninjas.com/studio/problems/reverse-an-array_8365444,Easy

# Brute
# T.C. -> O(log(n))
# S.C. -> O(log(n)) [Recursion stack space]


def helper(idx, arr, n):
    if idx == len(arr) // 2:
        return

    arr[idx], arr[n - idx - 1] = arr[n - idx - 1], arr[idx]
    helper(idx + 1, arr, n)


def reverseArray(n: int, nums: List[int]) -> List[int]:
    helper(0, nums, n)
    return nums
