# https://www.codingninjas.com/studio/problems/print-1-to-n_628290,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n) [Recursion stack space]


def helper(i, n, arr):
    if i == n + 1:
        return arr

    arr.append(i)
    return helper(i + 1, n, arr)


def printNos(x: int) -> List[int]:
    ans = []
    helper(1, x, ans)
    return ans
