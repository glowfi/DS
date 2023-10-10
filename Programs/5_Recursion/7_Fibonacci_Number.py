# https://www.codingninjas.com/studio/problems/print-fibonacci-series_7421617,Easy

# Brute
# T.C. -> O(n)
# S.C. -> O(n) [Recursion stack space]


def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def generateFibonacciNumbers(n: int) -> List[int]:
    ans = []
    for i in range(0, n):
        ans.append(fib(i))
    return ans


# Optimal
# T.C. -> O(n)
# S.C. -> O(1)


def fib(n):
    if n == 1:
        return [0]

    seclast, last = 0, 1
    ans = []
    ans.append(0)
    ans.append(1)
    for i in range(2, n):
        c = seclast + last
        ans.append(c)
        seclast = last
        last = c

    return ans


def generateFibonacciNumbers(n: int) -> List[int]:
    return fib(n)
