# https://www.codingninjas.com/studio/problems/n-to-1-without-loop_8357243,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n) [Recursion stack space]


def helper(i, arr):
    if i == 0:
        return arr

    arr.append(i)
    return helper(i - 1, arr)


def printNos(x: int) -> List[int]:
    ans = []
    helper(x, ans)
    return ans
