# https://www.codingninjas.com/studio/problems/reverse-stack-using-recursion_631875 , Easy

# Optimal
# T.C. -> O(log(n))
# S.C. -> O(log(n)) [Recursion stack]


def helper(idx, stack, n):
    if idx == n // 2:
        return

    stack[idx], stack[n - idx - 1] = stack[n - idx - 1], stack[idx]
    helper(idx + 1, stack, n)


def reverseStack(stack: List[int]) -> None:
    helper(0, stack, len(stack))
