# https://www.codingninjas.com/codestudio/problems/maximum-consecutive-ones_3843993,Easy

# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def consecutiveOnes(arr: List[int]) -> int:
    mx = 0
    c = 0
    if arr[0] == 1:
        c = 1

    for i in range(1, len(arr)):
        if arr[i] == 1 and arr[i - 1] == 1:
            c += 1
        elif arr[i] == 1 and arr[i - 1] != 1:
            c = 1
        mx = max(mx, c)

    return mx
